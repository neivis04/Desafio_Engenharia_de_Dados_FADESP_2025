import pandas as pd
import mysql.connector

# Conexão com o banco de dados
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    port="3306",
    password="cynthia.n06",        
    database="teste_fadesp"
)
cursor = conn.cursor()

# ========================
# Importar cnpq_tratado.csv
# ========================
print("Importando CNPq...")

df_cnpq = pd.read_csv("C:/Users/cynth/OneDrive/Área de Trabalho/Desafio_Eng._Dados_FADESP/data/processed/cnpq_tratado.csv")

for _, row in df_cnpq.iterrows():
    cursor.execute("""
        INSERT INTO cnpq_instituicoes (
            ano_censo, regiao, uf, sigla_uf, municipio, capital,
            tipo_org_academica, tipo_rede, categoria_adm,
            nome_instituicao, sigla, qt_doc_total, qt_tec_total
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['NU_ANO_CENSO'], row['NO_REGIAO_IES'], row['NO_UF_IES'], row['SG_UF_IES'], row['NO_MUNICIPIO_IES'],
        row['IN_CAPITAL_IES'], row['TP_ORGANIZACAO_ACADEMICA'], row['TP_REDE'], row['TP_CATEGORIA_ADMINISTRATIVA'],
        row['NOME_INSTITUICAO'], row['SG_IES'], row['QT_DOC_TOTAL'], row['QT_TEC_TOTAL']
    ))

conn.commit()
print("Dados CNPq importados com sucesso!")

# ========================
# Importar inep_tratado.csv
# ========================
print("Importando INEP...")

df_inep = pd.read_csv("C:/Users/cynth/OneDrive/Área de Trabalho/Desafio_Eng._Dados_FADESP/data/processed/inep_tratado.csv")

# Limpeza de valores
df_inep['VALOR_PAGO'] = (
    df_inep['VALOR_PAGO']
    .astype(str)
    .str.replace("R\$", "", regex=True)
    .str.replace(".", "", regex=False)
    .str.replace(",", ".", regex=False)
)

df_inep['VALOR_PAGO'] = pd.to_numeric(df_inep['VALOR_PAGO'], errors='coerce')

for _, row in df_inep.iterrows():
    cursor.execute("""
        INSERT INTO inep_bolsas (
            ano_referencia, processo, data_inicio, data_termino,
            beneficiario, modalidade, area_conhecimento,
            nome_instituicao, uf_origem, valor_pago
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['ANO_REFERENCIA'], row['PROCESSO'], row['DATA_INICIO_PROCESSO'], row['DATA_TERMINO_PROCESSO'],
        row['BENEFICIARIO'], row['MODALIDADE'], row['AREA_CONHECIMENTO'],
        row['NOME_INSTITUICAO'], row['SIGLA_UF_ORIGEM'], row['VALOR_PAGO']
    ))

conn.commit()
print("Dados INEP importados com sucesso!")

cursor.close()
conn.close()
