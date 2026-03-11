# Guia de Contribuição

## Padrões de nomenclatura
- Notebooks: `00_nome_da_camada.py` (prefixo numérico)
- Variáveis: `snake_case` (ex: `df_clientes_silver`)
- Constantes: `UPPER_CASE` (ex: `BUCKET_PATH`)

## Estrutura de um notebook
1. Imports
2. Constantes (paths, configs)
3. Funções reutilizáveis
4. Execução principal
5. Validação do resultado

## Regras para Pull Request
- Todo PR deve ter testes unitários cobrindo a transformação
- Rodar `flake8` localmente antes do push
- Descrever no PR: o que mudou, por que e como testar

## Padrões SQL
- Keywords em UPPER_CASE: `SELECT`, `FROM`, `WHERE`
- Aliases descritivos: `t.valor AS valor_transacao`
- Evitar `SELECT *` em produção

## Camadas da pipeline
- **Bronze:** dados brutos, nunca modificar
- **Silver:** limpeza, deduplicação e LGPD
- **Gold:** modelagem para consumo e ML
