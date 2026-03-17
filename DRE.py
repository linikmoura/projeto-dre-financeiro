import pandas as pd
from conexao_db import query_para_df

def gerar_dre(mes, ano):
    query = f"""
        SELECT 
            categoria,
            tipo,
            SUM(valor) AS total
        FROM lancamentos
        WHERE mes_referencia = {mes} AND ano_referencia = {ano}
        GROUP BY categoria, tipo
        ORDER BY tipo DESC, categoria
    """

    df = query_para_df(query)

    receita_bruta = df[df['categoria'] == 'Receita Bruta']['total'].sum()
    deducoes      = df[df['categoria'] == 'Deduções']['total'].sum()
    cmv           = df[df['categoria'] == 'CMV']['total'].sum()
    despesas      = df[df['categoria'] == 'Despesas Operacionais']['total'].sum()

    receita_liquida = receita_bruta - deducoes
    lucro_bruto     = receita_liquida - cmv
    lucro_liquido   = lucro_bruto - despesas

    print(f"\n{'='*45}")
    print(f"   DRE — {mes:02d}/{ano}")
    print(f"{'='*45}")
    print(f"  Receita Bruta:         R$ {receita_bruta:>12,.2f}")
    print(f"  (-) Deduções:          R$ {deducoes:>12,.2f}")
    print(f"  (=) Receita Líquida:   R$ {receita_liquida:>12,.2f}")
    print(f"  (-) CMV:               R$ {cmv:>12,.2f}")
    print(f"  (=) Lucro Bruto:       R$ {lucro_bruto:>12,.2f}")
    print(f"  (-) Despesas Oper.:    R$ {despesas:>12,.2f}")
    print(f"  (=) Lucro Líquido:     R$ {lucro_liquido:>12,.2f}")
    print(f"{'='*45}\n")

    return df, lucro_bruto, lucro_liquido

# Executar — troque o mês e ano desejado
gerar_dre(mes=6, ano=2025)