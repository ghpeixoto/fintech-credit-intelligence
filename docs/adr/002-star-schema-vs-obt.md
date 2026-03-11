# ADR 002 — Star Schema vs One Big Table (OBT) na Camada Gold

## Status
Aceito

## Contexto
A camada Gold precisa servir dois públicos distintos:
analistas de negócio (BI) e cientistas de dados (ML).

## Decisão
Implementar **ambos os modelos** na camada Gold:
- Star Schema para consumo via Power BI
- OBT para feature store do time de ML

## Justificativa
- Star Schema reduz complexidade de JOINs para analistas
- OBT otimiza leitura sequencial para modelos de ML
- Os dois modelos são derivados da mesma Silver, sem duplicação de lógica

## Alternativas consideradas
- **Apenas Star Schema:** insuficiente para ML, exige JOINs complexos
- **Apenas OBT:** dificulta queries analíticas ad-hoc no BI

## Consequências
- Maior volume de dados na camada Gold
- Necessidade de manter sincronismo entre os dois modelos
