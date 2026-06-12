from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.append("/mnt/c/Users/elangovan/Desktop/youtube comment section sentiment analysis")

from pipeline.run_pipeline import main_pipeline

dag = DAG(
    "youtube_sentiment_pipeline",
    start_date=datetime(2024,1,1),
    schedule="@hourly",
    catchup=False
)

run_pipeline = PythonOperator(
    task_id="run_pipeline",
    python_callable=main_pipeline,
    dag=dag
)