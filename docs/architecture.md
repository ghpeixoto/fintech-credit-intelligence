# Arquitetura — Fintech Credit Intelligence

## Visão Geral
```
S3 Raw (CSV)
    │
    ▼
┌─────────────────────────────────────────┐
│           DATABRICKS                    │
│                                         │
│  Bronze → Silver → Gold                 │
│  (Delta)   (LGPD)   (Star Schema + OBT) │
└─────────────────────────────────────────┘
    │
    ▼
Power BI (Dashboard)
ML Model (Feature Store)
```

## Componentes

| Componente | Tecnologia | Função |
|---|---|---|
| Data Lake | AWS S3 | Armazenamento raw e camadas |
| Processamento | Databricks + PySpark | Transformações Medallion |
| Formato | Delta Lake | ACID, Time Travel |
| Orquestração | Apache Airflow | Agendamento e monitoramento |
| Governança | Unity Catalog | Controle de acesso e metadados |
| CI/CD | GitHub Actions | Testes e linting automáticos |
| Visualização | Power BI | Dashboard gerencial |

## Decisões de Arquitetura
- [ADR 001 — Delta Lake vs Iceberg](adr/001-delta-vs-iceberg.md)
- [ADR 002 — Star Schema vs OBT](adr/002-star-schema-vs-obt.md)
