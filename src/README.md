### **Plano de Ação para o Desafio Técnico – FADESP 2025**

Este projeto tem como objetivo **analisar a relação entre a qualidade institucional e a produção científica no Brasil**, utilizando dados do **Censo da Educação Superior (INEP)** e do **CNPq (bolsistas)**. Através de um pipeline de dados completo — desde a extração, transformação e carga (ETL) até análises exploratórias e visualizações —, buscamos gerar insights sobre distribuição de bolsas, investimento e áreas de maior concentração científica.

```
DESAFIO_ENG_DADOS_FADESP/
│
├── notebooks/             # Notebooks de análise exploratória
│   ├── image/             # Pasta para salvar imagens dos gráficos
│   ├── analise_bolsistas.ipynb
│   ├── analise_instituicoes.ipynb
│   └── qtd_bolsas_area.ipynb
│
├── sql/                   # Scripts SQL para criação de tabelas
│   ├── criar_tabela.sql
│   └── importar_dados.py
│
├── src/                   # Código fonte do pipeline ETL
│   └── etl/
│       ├── extrair_dados.py
│       └── tratar_dados.py
│
├── data.zip                # Arquivo compactado contendo os dados brutos e os tratados
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação do projeto
└── .venv                   # Ambiente virtual (opcional)

```

## Tecnologias Utilizadas

- Python (Pandas, NumPy, SQLAlchemy, Plotly, Seaborn)
- MySQL
- Jupyter Notebook
- VSCode


## Pré-Requisitos

- Python 3.8 ou superior instalado
- MySQL instalado e em funcionamento
- Git (opcional, para clonar o repositório)


### 1️⃣ Clone o repositório (ou baixe os arquivos)

```bash
git clone https://github.com/seu-usuario/SEU-REPOSITORIO.git
cd DESAFIO_ENG_DADOS_FADESP
```


### 2️⃣ Crie e ative um ambiente virtual (recomendado)

```bash
python -m venv .venv
```
- Ativação no Windows:

```bash
.venv\Scripts\activate
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```


### 4️⃣ Configure o Banco de Dados MySQL

1. Crie um banco de dados no MySQL (exemplo):

```sql
CREATE DATABASE desafio_fadesp;
```

1. Execute o script SQL localizado em `sql/criar_tabela.sql` para criar as tabelas necessárias.

Você pode fazer isso pelo terminal MySQL, DBeaver ou diretamente pelo script `importar_dados.py` que automatiza a carga dos dados no banco.


### 5️⃣ Execute o Pipeline ETL

O pipeline ETL está na pasta `src/etl`:

- **1. Extração dos dados**

```bash
python src/etl/extrair_dados.py
```

- **2. Tratamento e transformação dos dados**

```bash
python src/etl/tratar_dados.py
```

Estes scripts irão:

- Extrair os dados contidos no arquivo `data.zip`
- Realizar limpeza, normalização e padronização
- Popular as tabelas no banco MySQL


### 6️⃣ Análises e Visualizações

Acesse a pasta `notebooks/` e execute os notebooks:

- `analise_bolsistas.ipynb` → Análise dos bolsistas por instituição
- `analise_instituicoes.ipynb` → Análise dos valores investidos por instituição
- `qtd_bolsas_area.ipynb` → Análise das bolsas por área de conhecimento

As imagens geradas ficam armazenadas automaticamente na pasta `notebooks/image`.


## 💡 Resultados Gerados

- Distribuição dos bolsistas por instituição
- Volume de investimento por instituição
- Áreas do conhecimento com maior concentração de bolsas
- Visualizações claras e insights sobre os dados


## 🏁 Conclusão

Este projeto simula um pipeline completo de dados, desde a ingestão até a análise, permitindo a obtenção de insights relevantes para orientar decisões no fomento à pesquisa no Brasil.
