from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="ecommerce_data_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:

    spark_transform = BashOperator(
        task_id="spark_transform_orders",
        bash_command="spark-submit /Users/shaik.noushad/ecommerce_data_pipeline/scripts/transform/spark_transform_orders.py"
    )

    load_postgres = BashOperator(
        task_id="load_to_postgres",
        bash_command="python /Users/shaik.noushad/ecommerce_data_pipeline/scripts/load/load_to_postgres.py"
    )

    spark_transform >> load_postgres

