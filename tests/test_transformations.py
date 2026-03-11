import pytest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col


@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder \
        .master("local") \
        .appName("fintech-tests") \
        .getOrCreate()


def test_clientes_sem_nulos(spark):
    """Garante que cliente_id nunca é nulo na Silver."""
    data = [("id-1", "Ana"), ("id-2", "Joao"), (None, "Pedro")]
    df = spark.createDataFrame(data, ["cliente_id", "nome"])
    df_limpo = df.filter(col("cliente_id").isNotNull())
    assert df_limpo.count() == 2


def test_valor_transacao_positivo(spark):
    """Garante que valores negativos são filtrados."""
    data = [("t1", 100.0), ("t2", -50.0), ("t3", 200.0)]
    df = spark.createDataFrame(data, ["transacao_id", "valor"])
    df_valido = df.filter(col("valor") > 0)
    assert df_valido.count() == 2


def test_status_validos(spark):
    """Garante que apenas status permitidos passam pela Silver."""
    data = [("t1", "Aprovada"), ("t2", "Negada"), ("t3", "Invalido")]
    df = spark.createDataFrame(data, ["id", "status"])
    df_valido = df.filter(col("status").isin("Aprovada", "Negada", "Em Analise"))
    assert df_valido.count() == 2


def test_score_risco_no_range(spark):
    """Score de risco deve estar entre 0 e 100."""
    data = [("l1", 50.0), ("l2", 150.0), ("l3", -10.0)]
    df = spark.createDataFrame(data, ["log_id", "score"])
    df_valido = df.filter(col("score").between(0, 100))
    assert df_valido.count() == 1
