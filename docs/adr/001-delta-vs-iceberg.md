# ADR 001 — Delta Lake vs Apache Iceberg

## Status
Aceito

## Contexto
Precisávamos escolher um formato de tabela open source para armazenar
os dados nas camadas Bronze, Silver e Gold no S3.

## Decisão
Escolhemos **Delta Lake** como formato padrão para todas as camadas.

## Justificativa
- Integração nativa com Databricks sem configuração adicional
- ACID transactions garantindo consistência nos dados financeiros
- Time Travel permite auditoria de alterações (requisito regulatório)
- Melhor suporte a MERGE para deduplicação na camada Silver
- Ecossistema mais maduro e documentação mais ampla

## Alternativas consideradas
- **Apache Iceberg:** excelente para multi-engine, mas requer
  configuração adicional no Databricks e menor suporte nativo
- **Apache Hudi:** foco em streaming, overhead desnecessário
  para o volume atual do projeto

## Consequências
- Vendor lock-in parcial com Databricks
- Facilidade para migrar para Iceberg futuramente se necessário
