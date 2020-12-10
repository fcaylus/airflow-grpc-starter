from datetime import timedelta

from airflow import DAG
from airflow.providers.grpc.operators.grpc import GrpcOperator
from airflow.utils.dates import days_ago
from proto.ping_pb2_grpc import PingServiceStub
from proto.ping_pb2 import PingRequest


def response_handler(response, context):
    print("Response received from gRPC")
    print("Response : " + response.response)


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'ping_grpc',
    default_args=default_args,
    description='Ping gRPC service',
    schedule_interval=timedelta(days=1),
)

operator = GrpcOperator(
    task_id='grpc_request',
    grpc_conn_id='grpc_default',
    stub_class=PingServiceStub,
    call_func='ping',
    data={'request': PingRequest()},
    response_callback=response_handler,
    streaming=False,
    dag=dag,
)
