import pandas as pd
from conexao_db import query_para_df

def despesas_por_centro_custo(ano):
    query = f"""
        SELECT 
            mes_referencia,
            centro_custo,
            SUM(valor) AS total_despesa
        FROM lancamentos
        WHERE tipo = 'despesa'
        AND ano_referencia = {ano}
        GROUP BY mes_referencia, centro_custo
        ORDER BY mes_referencia, total_despesa DESC
    """

    df = query_para_df(query)

    # Girar a tabela: meses nas linhas, centros de custo nas colunas
    pivot = df.pivot_table(
        index='mes_referencia',
        columns='centro_custo',
        values='total_despesa',
        aggfunc='sum'
    ).fillna(0)

    pivot.columns.name = None
    pivot.index = [f"Mês {m:02d}" for m in pivot.index]

    # Adicionar total por mês
    pivot['TOTAL GERAL'] = pivot.sum(axis=1)

    # Adicionar total por centro de custo
    pivot.loc['TOTAL ANUAL'] = pivot.sum()

    print(f"\n{'='*75}")
    print(f"   DESPESAS POR CENTRO DE CUSTO — {ano}")
    print(f"{'='*75}")
    print(pivot.to_string(float_format=lambda x: f"R$ {x:,.2f}"))
    print(f"{'='*75}\n")

    return pivot

def exportar_centro_custo(ano):
    df = despesas_por_centro_custo(ano)

    caminho = f"despesas_centro_custo_{ano}.xlsx"

    with pd.ExcelWriter(caminho, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Centro de Custo')

    print(f"✅ Relatório exportado: {caminho}")

# Executar
despesas_por_centro_custo(ano=2025)
exportar_centro_custo(ano=2025)