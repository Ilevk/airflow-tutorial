from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator
from pendulum import datetime


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
def example_operator_dag():
    logan_hi_task = PythonOperator(
        task_id="logan_hi_task",
        python_callable=example_task,
        op_kwargs={"name": "Logan"},
    )
    david_hi_task = PythonOperator(
        task_id="david_hi_task",
        python_callable=example_task,
        op_kwargs={"name": "David"},
    )

    logan_hi_task >> david_hi_task


example_operator_dag()
