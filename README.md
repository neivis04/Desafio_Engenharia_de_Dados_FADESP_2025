# Desafio_Engenharia_de_Dados_FADESP_2025

# **Plano de Ação para o Desafio Técnico – FADESP 2025**

### 🎯 Objetivo Geral

Estabelecer relações entre a qualidade institucional e a produção científica brasileira, com base nos dados do Censo da Educação Superior (INEP) e do CNPq (bolsistas), por meio de análise exploratória, modelagem preditiva e visualização de dados, utilizando Python, Jupyter e MySQL.

---

### 🔧 Tecnologias e Ferramentas

- **Python**: manipulação e análise de dados (pandas, numpy, scipy, statsmodels)
- **Jupyter Notebook**: organização do processo analítico com documentação
- **MySQL**: criação de banco relacional para armazenamento e consultas SQL
- **Plotly / Seaborn**: visualizações interativas e informativas

---

## 🧭 Etapas

### **Extração e Engenharia de Dados**

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

### **Visualizações e Comunicação**

### Tarefas:

- Criar dashboards e gráficos interativos com `plotly` e `seaborn`.
- Verificar quais áreas recebem mais apoio.
- Descobrir quais instituições concentram mais bolsistas.
- Caracterizar as IES que mais recebem bolsas.
- Documentar as análises e gráficos nos notebooks.

### Resultado Esperado:

- Visualizações claras e impactantes.
- Caderno final de análise pronto.


## **Resultados Esperados e Entregáveis**

- ✔ Banco de dados MySQL com os dados tratados
- ✔ Scripts de ETL e notebooks organizados
- ✔ Visualizações estatísticas e geográficas
- ✔ `README.md` com instruções de uso
- ✔ Apresentação curta com metodologia, desafios e descobertas

## **Importância do Processo**

Esse fluxo representa um **pipeline completo de dados**:

- Do **dado cru** à **informação estruturada**.
- Da **análise descritiva** à **decisão baseada em evidência**.
