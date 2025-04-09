from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def print_hello():
    print("Olá, mundo! Este é um exemplo de DAG do Airflow.")

with DAG(
    'hello_world',
    default_args=default_args,
    description='Uma DAG simples de exemplo',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['exemplo'],
) as dag:

    t1 = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello,
    )

    t2 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t1 >> t2  # Define a ordem de execução: t1 executa antes de t2 