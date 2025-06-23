import pandas as pd
import numpy as np

inep = pd.read_csv(
    "C:/Users/cynth/OneDrive/Área de Trabalho/Desafio_Eng._Dados_FADESP/data/raw/dados_bolsistas_CNPQ_2023.csv",
    sep=";",
    encoding="utf-8-sig",
    low_memory=False
)

cnpq = pd.read_csv(
    "C:/Users/cynth/OneDrive/Área de Trabalho/Desafio_Eng._Dados_FADESP/data/raw/dados_ens._sup._2023.csv",
    sep=";",
    encoding="latin1",
    low_memory=False
)

def tratar_dados(df, nome_base=""):
    # Remover colunas totalmente nulas
    df = df.dropna(axis=1, how='all')

    # Remover colunas duplicadas
    df = df.loc[:, ~df.columns.duplicated()]

    # Padronizar nomes das colunas
    df.columns = (
        df.columns.str.strip()
                  .str.upper()
                  .str.normalize("NFKD")
                  .str.encode("ascii", errors="ignore")
                  .str.decode("utf-8")
                  .str.replace(" ", "_")
    )

    # Normalizar strings
    obj_cols = df.select_dtypes(include='object').columns
    for col in obj_cols:
        df[col] = df[col].astype(str).str.strip().str.upper()

    # Preencher valores nulos
    df[obj_cols] = df[obj_cols].replace({'NAN': '', 'NONE': ''}).fillna('')
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[num_cols] = df[num_cols].fillna(0).round(0).astype(int)

    # Converter datas
    data_cols = [col for col in df.columns if "DATA" in col]
    for col in data_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce', dayfirst=True)

    # Remover duplicadas
    df = df.drop_duplicates()

    # Renomear colunas específicas
    col_renomear = {
        'NO_IES': 'NOME_INSTITUICAO',
        'QT_DOC_EX_FEMI': 'DOCENTES_FEMININO',
        'QT_DOC_EX_DOUT': 'DOCENTES_DOUTORES',
        'INSTITUICAO_DESTINO': 'NOME_INSTITUICAO',
        'GRANDE_AREA': 'AREA_CONHECIMENTO'
    }
    df = df.rename(columns=col_renomear)

    # Remover "R$" e ponto de milhar, trocar vírgula por ponto e converter para float
    inep["VALOR_PAGO"] = (
    inep["VALOR_PAGO"]
    .str.replace("R\$\s?", "", regex=True)
    .str.replace(".", "", regex=False)
    .str.replace(",", ".", regex=False)
    .astype(float)
)

    # Excluir colunas irrelevantes
    col_excluir = [
        'CO_REGIAO_IES', 'CO_UF_IES', 'CO_MUNICIPIO_IES', 'CO_MESORREGIAO_IES',
        'CO_MICRORREGIAO_IES', 'CO_MANTENEDORA', 'CO_IES', 'DS_ENDERECO_IES',
        'DS_COMPLEMENTO_ENDERECO_IES', 'DS_NUMERO_ENDERECO_IES', 'NU_CEP_IES',
        'SIGLA_INSTITUICAO_MACRO', 'SIGLA_INSTITUICAO_DESTINO',
        'PALAVRA_CHAVE', 'UO'
    ]
    df = df.drop(columns=[col for col in col_excluir if col in df.columns], errors='ignore')

    print(f"\n {nome_base} tratado com {df.shape[0]} linhas e {df.shape[1]} colunas.")
    return df

inep = tratar_dados(inep, nome_base="INEP")
cnpq = tratar_dados(cnpq, nome_base="CNPq")

inep.to_csv("C:/Users/cynth/OneDrive/Área de Trabalho/Desafio_Eng._Dados_FADESP/data/processed/inep_tratado.csv", index=False, encoding="utf-8-sig")
cnpq.to_csv("C:/Users/cynth/OneDrive/Área de Trabalho/Desafio_Eng._Dados_FADESP/data/processed/cnpq_tratado.csv", index=False, encoding="utf-8-sig")
