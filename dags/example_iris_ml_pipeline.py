from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from pendulum import datetime

from module import train


@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    doc_md=__doc__,
    default_args={"owner": "Astro", "retries": 3},
    tags=["example"],
)
def example_iris_ml_pipeline():
    start_task = EmptyOperator(task_id="start_task")
    train_task = PythonOperator(
        task_id="train_task",
        python_callable=train.train_fn_iris,
    )
    model_create_task = PythonOperator(
        task_id="model_create_task",
        python_callable=train.create_model_version,
        op_kwargs={"model_name": "iris_model"},
    )
    model_transition_task = PythonOperator(
        task_id="model_transition_task",
        python_callable=train.transition_model_stage,
        op_kwargs={"model_name": "iris_model"},
    )
    end_task = EmptyOperator(task_id="end_task")

    start_task >> [train_task >> model_create_task >> model_transition_task] >> end_task


example_iris_ml_pipeline()
