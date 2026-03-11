# Fintech Credit Intelligence 🏦

Pipeline de Inteligência de Crédito e Prevenção a Fraude.

## Arquitetura
`S3 Raw → Bronze → Silver → Gold → Power BI / ML`

## Stack
- **AWS S3** — Data Lake
- **Databricks** — Processamento PySpark + Delta Lake
- **Apache Airflow** — Orquestração
- **GitHub Actions** — CI/CD

## Como rodar o Airflow localmente
```bash
git clone https://github.com/ghpeixoto/fintech-credit-intelligence
cd fintech-credit-intelligence
mkdir logs plugins
echo "AIRFLOW_UID=$(id -u)" > .env
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.1/docker-compose.yaml'
docker compose up airflow-init
docker compose up -d
```
Acesse http://localhost:8080 — usuário: `airflow` / senha: `airflow`

## Estrutura
```
├── dags/               # DAGs do Airflow
├── notebooks/          # Notebooks Databricks
├── tests/              # Testes unitários PySpark
├── docs/               # ADRs e dicionário de dados
└── .github/workflows/  # CI/CD GitHub Actions
```
