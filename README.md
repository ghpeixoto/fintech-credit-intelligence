# 🏦 Fintech Credit Intelligence

Pipeline de Inteligência de Crédito e Prevenção a Fraude construída 
com arquitetura Medallion (Bronze → Silver → Gold).

## 🏗️ Arquitetura
```
S3 Raw (CSV)
     │
     ▼
┌──────────────────────────────────────────┐
│            DATABRICKS                    │
│  Bronze → Silver (LGPD) → Gold           │
│  (Delta)                (Star Schema+OBT)│
└──────────────────────────────────────────┘
     │
     ▼
Airflow (Orquestração) + Power BI (Dashboard)
```

## 🛠️ Stack Tecnológica

| Camada | Tecnologia |
|---|---|
| Data Lake | AWS S3 |
| Processamento | Databricks + PySpark + Delta Lake |
| Governança | Unity Catalog |
| Orquestração | Apache Airflow (Docker) |
| CI/CD | GitHub Actions |
| Visualização | Power BI |

## 📁 Estrutura do Projeto
```
├── dags/                   # DAGs do Airflow
│   └── fintech_pipeline.py # Pipeline Bronze→Silver→Gold
├── notebooks/              # Notebooks Databricks
│   ├── 01_bronze_raw_ingestion.py
│   ├── 02_silver_transformation.py
│   └── 03_gold_modeling.py
├── tests/                  # Testes unitários PySpark
│   └── test_transformations.py
├── docs/                   # Documentação técnica
│   ├── adr/                # Architecture Decision Records
│   │   ├── 001-delta-vs-iceberg.md
│   │   └── 002-star-schema-vs-obt.md
│   ├── data-dictionary.md  # Dicionário de dados
│   └── architecture.md     # Visão geral da arquitetura
├── .github/workflows/      # CI/CD
│   └── ci.yml
└── CONTRIBUTING.md         # Guia de contribuição
```

## 🚀 Como rodar o Airflow localmente
```bash
git clone https://github.com/ghpeixoto/fintech-credit-intelligence
cd fintech-credit-intelligence
mkdir logs plugins
echo "AIRFLOW_UID=$(id -u)" > .env
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.1/docker-compose.yaml'
docker compose up airflow-init
docker compose up -d
```

Acesse **http://localhost:8080** — usuário: `airflow` / senha: `airflow`

## 📊 Camadas da Pipeline

### 🥉 Bronze
- Ingestão raw dos CSVs do S3
- Adição de metadata (`_ingested_at`, `_source`)
- Formato Delta Lake

### 🥈 Silver
- Deduplicação e limpeza de dados
- Anonimização de PII com SHA-256 (LGPD)
- Validação de qualidade de dados

### 🥇 Gold
- **Star Schema:** `dim_cliente` + `fato_transacoes`
- **OBT:** `obt_fraude_features` com 23 features para ML
- Flag de alto risco por cliente

## ✅ CI/CD
A cada push na branch `main` o GitHub Actions executa:
- Linting com `flake8`
- Testes unitários com `pytest`
