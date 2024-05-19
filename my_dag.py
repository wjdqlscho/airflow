from airflow import DAG
from airflow.operators.python_operator import PythonOperator # type: ignore
from datetime import datetime, timedelta

def my_task():
    print("Hello, Airflow!")

default_args = {
    'owner': 'jungbin1486',
    'depends_on_past': False,
    'email': ['jungbin1486@hanmail.net'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'my_dag',
    default_args=default_args,
    description='A simple DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 5, 20),
    catchup=False,
)

task1 = PythonOperator(
    task_id='my_task',
    python_callable=my_task,
    dag=dag,
)
task1