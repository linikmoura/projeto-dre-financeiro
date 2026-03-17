import pandas as pd
from conexao_db import conectar

def carregar_csv_para_mysql(caminho_csv):
    df = pd.read_csv(caminho_csv, sep=';', parse_dates=['data_lancamento'])

    df['mes_referencia'] = df['data_lancamento'].dt.month
    df['ano_referencia'] = df['data_lancamento'].dt.year

    conn = conectar()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO lancamentos 
            (data_lancamento, descricao, categoria, tipo, valor, centro_custo, mes_referencia, ano_referencia)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            str(row['data_lancamento'].date()),
            row['descricao'],
            row['categoria'],
            row['tipo'],
            float(row['valor']),
            row['centro_custo'],
            int(row['mes_referencia']),
            int(row['ano_referencia'])
        ))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"{len(df)} registros inseridos com sucesso!")

# Executar
carregar_csv_para_mysql(r'C:\Users\Usuario\Desktop\DRE\lancamentos_financeiros.csv')