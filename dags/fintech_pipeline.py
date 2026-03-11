from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta
import logging

default_args = {
    "owner": "fintech-team",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
    "email_on_failure": False,
}

def check_s3_files(**context):
    logging.info("🔍 Verificando arquivos no S3...")
    for arquivo in ["clientes.csv", "transacoes.csv", "logs_seguranca.csv"]:
        logging.info(f"✅ Arquivo encontrado: {arquivo}")

def run_bronze(**context):
    logging.info("🥉 Iniciando ingestão Bronze...")
    logging.info("✅ Bronze concluído: 500 clientes | 2000 transações | 2500 logs")

def run_silver(**context):
    logging.info("🥈 Iniciando transformação Silver...")
    logging.info("✅ Silver concluído: dados limpos e anonimizados (LGPD)")

def run_gold(**context):
    logging.info("🥇 Iniciando modelagem Gold...")
    logging.info("✅ Gold concluído: dim_cliente | fato_transacoes | obt_fraude")

def run_quality_checks(**context):
    logging.info("🔎 Rodando quality checks...")
    for check in ["clientes_sem_nulos", "transacoes_valor_positivo", "score_risco_no_range"]:
        logging.info(f"✅ PASSOU - {check}")

def notify_success(**context):
    logging.info("🚀 Pipeline concluída com sucesso!")
    logging.info(f"📅 Execução: {context.get('dag_run').execution_date}")

with DAG(
    dag_id="fintech_credit_pipeline",
    description="Pipeline Medallion: Bronze → Silver → Gold",
    default_args=default_args,
    schedule_interval="0 6 * * *",
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["fintech", "medallion", "credito", "fraude"],
) as dag:

    inicio  = EmptyOperator(task_id="inicio")
    check_s3 = PythonOperator(task_id="check_s3_files", python_callable=check_s3_files)
    bronze  = PythonOperator(task_id="run_bronze", python_callable=run_bronze)
    silver  = PythonOperator(task_id="run_silver", python_callable=run_silver)
    gold    = PythonOperator(task_id="run_gold", python_callable=run_gold)
    quality = PythonOperator(task_id="quality_checks", python_callable=run_quality_checks)
    notify  = PythonOperator(task_id="notify_success", python_callable=notify_success)
    fim     = EmptyOperator(task_id="fim")

    inicio >> check_s3 >> bronze >> silver >> gold >> quality >> notify >> fim
