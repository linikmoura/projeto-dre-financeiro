import pandas as pd
from DRE import gerar_dre
from fluxo_caixa import gerar_fluxo_caixa

def exportar_relatorio(mes, ano):
    df_dre, lucro_bruto, lucro_liquido = gerar_dre(mes, ano)
    df_fluxo = gerar_fluxo_caixa(ano)

    caminho = f"relatorio_{mes:02d}_{ano}.xlsx"

    with pd.ExcelWriter(caminho, engine='openpyxl') as writer:
        df_dre.to_excel(writer, sheet_name='DRE', index=False)
        df_fluxo.to_excel(writer, sheet_name='Fluxo de Caixa')

    print(f"✅ Relatório exportado: {caminho}")

# Executar
exportar_relatorio(mes=1, ano=2025)