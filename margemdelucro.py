import pandas as pd
from conexao_db import query_para_df

def analise_margem(ano):
    query = f"""
        SELECT 
            mes_referencia,
            tipo,
            SUM(valor) AS total
        FROM lancamentos
        WHERE ano_referencia = {ano}
        GROUP BY mes_referencia, tipo
        ORDER BY mes_referencia
    """

    df = query_para_df(query)

    # Girar a tabela: receita e despesa como colunas
    pivot = df.pivot_table(
        index='mes_referencia',
        columns='tipo',
        values='total',
        aggfunc='sum'
    ).fillna(0)

    pivot.columns.name = None

    # Cálculos
    pivot['lucro_liquido']     = pivot['receita'] - pivot['despesa']
    pivot['margem_lucro_%']    = (pivot['lucro_liquido'] / pivot['receita'] * 100).round(2)
    pivot['variacao_lucro_%']  = pivot['lucro_liquido'].pct_change().mul(100).round(2)

    # Renomear índice
    pivot.index = [f"Mês {m:02d}" for m in pivot.index]

    # Totais anuais
    total_receita  = pivot['receita'].sum()
    total_despesa  = pivot['despesa'].sum()
    total_lucro    = pivot['lucro_liquido'].sum()
    margem_anual   = (total_lucro / total_receita * 100).round(2)

    # Exibir no terminal
    print(f"\n{'='*80}")
    print(f"   RECEITAS x DESPESAS x MARGEM DE LUCRO — {ano}")
    print(f"{'='*80}")
    print(pivot.to_string(float_format=lambda x: f"{x:,.2f}"))
    print(f"{'='*80}")
    print(f"  Total Receitas:    R$ {total_receita:>12,.2f}")
    print(f"  Total Despesas:    R$ {total_despesa:>12,.2f}")
    print(f"  Lucro Líquido:     R$ {total_lucro:>12,.2f}")
    print(f"  Margem Anual:          {margem_anual:>11.2f}%")
    print(f"{'='*80}\n")

    return pivot, total_receita, total_despesa, total_lucro, margem_anual


def exportar_margem(ano):
    pivot, total_receita, total_despesa, total_lucro, margem_anual = analise_margem(ano)

    caminho = f"margem_lucro_{ano}.xlsx"

    with pd.ExcelWriter(caminho, engine='openpyxl') as writer:
        # Aba principal
        pivot.to_excel(writer, sheet_name='Margem de Lucro')

        # Aba resumo anual
        resumo = pd.DataFrame({
            'Indicador': ['Total Receitas', 'Total Despesas', 'Lucro Líquido', 'Margem Anual (%)'],
            'Valor': [
                f"R$ {total_receita:,.2f}",
                f"R$ {total_despesa:,.2f}",
                f"R$ {total_lucro:,.2f}",
                f"{margem_anual:.2f}%"
            ]
        })
        resumo.to_excel(writer, sheet_name='Resumo Anual', index=False)

    print(f"✅ Relatório exportado: {caminho}")

    # Alertas automáticos
    print(f"\n{'='*80}")
    print("   📋 ALERTAS AUTOMÁTICOS")
    print(f"{'='*80}")

    for mes, row in pivot.iterrows():
        # Alerta se margem abaixo de 20%
        if row['margem_lucro_%'] < 20:
            print(f"  ⚠️  {mes}: Margem baixa — {row['margem_lucro_%']:.2f}%")

        # Alerta se lucro caiu mais de 10% em relação ao mês anterior
        if pd.notna(row['variacao_lucro_%']) and row['variacao_lucro_%'] < -10:
            print(f"  🔴 {mes}: Lucro caiu {abs(row['variacao_lucro_%']):.2f}% em relação ao mês anterior")

        # Alerta se despesa maior que receita
        if row['despesa'] > row['receita']:
            print(f"  🚨 {mes}: DESPESA MAIOR QUE RECEITA!")

    print(f"{'='*80}\n")


# Executar
analise_margem(ano=2025)
exportar_margem(ano=2025)