# **Plano de Ação para o Desafio Técnico – FADESP 2025**

## 🎯 Objetivo Geral

Estabelecer relações entre a qualidade institucional e a produção científica brasileira, com base nos dados do Censo da Educação Superior (INEP) e do CNPq (bolsistas), por meio de análise exploratória, modelagem preditiva e visualização de dados, utilizando Python, Jupyter e MySQL.


## 🔧 Tecnologias e Ferramentas

- **Python**: manipulação e análise de dados (pandas, numpy, scipy, statsmodels)
- **Jupyter Notebook**: organização do processo analítico com documentação
- **MySQL**: criação de banco relacional para armazenamento e consultas SQL
- **Plotly / Seaborn**: visualizações interativas e informativas


## Etapas

## **1. Extração e Engenharia de Dados**

### Tarefas:

- Carregar os dois datasets (`INEP` e `CNPq`) no Python.
- Analisar colunas relevantes e realizar seleção inicial.
- Tratar:
    - Nomes inconsistentes,
    - Dados faltantes,
    - Conversão de formatos (datas, números).
- Normalizar instituições (nome, UF, tipo).
- Construir banco MySQL relacional:
    - Tabelas: `instituicoes`, `pesquisadores`, `bolsas`, `caracteristicas_ies`, etc.
    - Importação de dados com `SQLAlchemy` ou `pymysql`.
- Documentar todo o processo de ETL.

### Resultado:

- Banco de dados relacional bem estruturado pronto para análise.
- Dados limpos e padronizados.

## **2. Visualizações e Comunicação**

### Tarefas:

- Criar dashboards e gráficos interativos com `plotly` e `seaborn`.
- Verificar quais áreas recebem mais apoio.
- Descobrir quais instituições concentram mais bolsistas.
- Caracterizar as IES que mais recebem bolsas.
- Documentar as análises e gráficos nos notebooks.

### Resultado Esperado:

- Visualizações claras e impactantes.
- Caderno final de análise pronto.

## **3. Resultados Esperados e Entregáveis**

- ✔ Banco de dados MySQL com os dados tratados
- ✔ Scripts de ETL e notebooks organizados
- ✔ Visualizações estatísticas e geográficas
- ✔ `README.md` com instruções de uso
- ✔ Apresentação curta com metodologia, desafios e descobertas

## **4. Principais Desafios**

- Alto volume de dados com estrutura inconsistente.
- Necessidade de normalização de instituições (nomes diferentes para a mesma IES).
- Conversão e padronização de valores monetários.

## **5. Descobertas Relevantes**

- Algumas áreas concentram grande parte das bolsas (ex: Ciências Humanas e Exatas).
- Instituições federais concentram o maior valor investido.
- Relação entre localização (região e UF) e investimento recebido.

## **6. Recomendações Baseadas nos Dados**

- Reforçar apoio a instituições com menor captação de bolsas, promovendo equidade.
- Incentivar áreas estratégicas ainda com baixa cobertura de bolsas.

