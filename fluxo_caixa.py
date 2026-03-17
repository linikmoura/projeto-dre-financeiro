import pandas as pd
from conexao_db import query_para_df

def gerar_fluxo_caixa(ano):
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

    pivot = df.pivot_table(
        index='mes_referencia',
        columns='tipo',
        values='total',
        aggfunc='sum'
    ).fillna(0)

    pivot.columns.name = None
    pivot['saldo_mensal']    = pivot['receita'] - pivot['despesa']
    pivot['saldo_acumulado'] = pivot['saldo_mensal'].cumsum()
    pivot.index = [f"Mês {m:02d}" for m in pivot.index]

    print(f"\n{'='*65}")
    print(f"   FLUXO DE CAIXA — {ano}")
    print(f"{'='*65}")
    print(pivot.to_string())
    print(f"{'='*65}\n")

    return pivot

# Executar
gerar_fluxo_caixa(ano=2025)