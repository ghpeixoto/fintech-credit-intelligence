# Dicionário de Dados — Fintech Credit Intelligence

## Camada Silver

### `silver/clientes`
| Campo | Tipo | Descrição |
|---|---|---|
| cliente_id | string | Identificador único do cliente (UUID) |
| nome | string | Nome completo em maiúsculas |
| cpf_anonimizado | string | Hash SHA-256 do CPF (LGPD) |
| email_anonimizado | string | Hash SHA-256 do email (LGPD) |
| data_nascimento | date | Data de nascimento |
| cidade | string | Cidade em maiúsculas |
| _silver_at | timestamp | Data de processamento na Silver |

### `silver/transacoes`
| Campo | Tipo | Descrição |
|---|---|---|
| transacao_id | string | Identificador único da transação |
| cliente_id | string | FK para clientes |
| valor | double | Valor da transação (sempre positivo) |
| data_hora | timestamp | Data e hora da transação |
| status | string | Aprovada / Negada / Em Analise |
| tipo_operacao | string | Emprestimo / Cartao de Credito / Financiamento |

### `silver/logs_seguranca`
| Campo | Tipo | Descrição |
|---|---|---|
| log_id | string | Identificador único do log |
| cliente_id | string | FK para clientes |
| ip_origem | string | Hash SHA-256 do IP (LGPD) |
| dispositivo | string | iOS / Android / Web |
| data_hora_login | timestamp | Data e hora do login |
| sucesso_login | boolean | True se login bem-sucedido |
| score_risco_dispositivo | double | Score de 0 a 100 |

## Camada Gold

### `gold/obt_fraude_features`
| Campo | Tipo | Descrição |
|---|---|---|
| cliente_id | string | Identificador único do cliente |
| total_transacoes | long | Total de transações do cliente |
| taxa_aprovacao | double | % de transações aprovadas |
| taxa_falha_login | double | % de logins com falha |
| score_risco_medio | double | Média do score de risco |
| score_risco_maximo | double | Maior score de risco registrado |
| qtd_dispositivos_distintos | long | Quantidade de dispositivos usados |
| flag_alto_risco | boolean | True se cliente é de alto risco |
