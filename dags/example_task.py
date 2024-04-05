from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator
from pendulum import datetime


@task
def example_task(name: str):
    print("Hello , World!", name)


@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    doc_md=__doc__,
    default_args={"owner": "Astro", "retries": 3},
    tags=["example"],
)
def example_task_dag():
    example_task("Logan")
    example_task("David")


example_task_dag()
