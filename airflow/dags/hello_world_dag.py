from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from hello_function import hello_world


default_args = {
    'owner': 'ruy',
    'start_date': datetime(2025, 4, 1),
}

with DAG(
    'hello_world_dag',
    default_args=default_args,
    schedule_interval='@once',
    catchup=False,
) as dag:
    
    hello_task = PythonOperator(
        task_id='hello_world_task',
        python_callable=hello_world
    )
