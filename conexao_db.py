import pymysql
import pandas as pd

def conectar():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Lixo1205@",
        database="financeiro"
    )
    return conn

def query_para_df(query):
    conn = conectar()
    df = pd.read_sql(query, conn)
    conn.close()
    return df