FROM apache/airflow:1.10.12-python3.6

USER airflow

COPY ./requirements.txt ./
RUN pip install --user -r requirements.txt
COPY ./src ./
