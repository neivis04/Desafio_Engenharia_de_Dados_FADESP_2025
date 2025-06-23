import pandas as pd

# Leitura das bases de dados cruas
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

# Exibir as primeiras linhas de cada base
print("Visualização inicial do INEP:")
print(inep.head(), "\n")

print("Visualização inicial do CNPq:")
print(cnpq.head(), "\n")

# Exibir estrutura das bases
print("Estrutura do INEP:")
print(inep.info(), "\n")

print("Estrutura do CNPq:")
print(cnpq.info(), "\n")

# Exibir número de colunas totalmente nulas
print("Colunas totalmente nulas no INEP:")
print(inep.columns[inep.isnull().all()])

print("\n Colunas totalmente nulas no CNPq:")
print(cnpq.columns[cnpq.isnull().all()])

# Quantidade total de valores nulos por coluna
print("\n Valores faltantes por coluna - INEP:")
print(inep.isnull().sum())

print("\n Valores faltantes por coluna - CNPq:")
print(cnpq.isnull().sum())

# Tamanho das bases
print(f"\n INEP: {inep.shape[0]} linhas e {inep.shape[1]} colunas")
print(f" CNPq: {cnpq.shape[0]} linhas e {cnpq.shape[1]} colunas")
