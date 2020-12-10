from datetime import timedelta

from airflow import DAG
from airflow.providers.grpc.operators.grpc import GrpcOperator
from airflow.utils.dates import days_ago

# These files are generated by the protobuf compiler
from proto.ping_pb2_grpc import PingServiceStub
from proto.ping_pb2 import PingRequest


def response_handler(response, context):
    print("Response received from gRPC")
    print("Response : " + response.message)


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'retries': 0
}

dag = DAG(
    'ping_grpc',
    default_args=default_args,
    description='Ping gRPC service',
    schedule_interval=timedelta(days=1),
)

"""
Create a new gRPC Operator
"""
operator = GrpcOperator(
    dag=dag,
    task_id='grpc_request',
    # gRPC Connection ID used for this operator.
    # A connection of type "GRPC Connection" and with the same id should be configured in the Airflow Admin panel
    # If omitted, defaults to "grpc_default"
    grpc_conn_id='grpc_default',
    # gRPC service stub class (must be imported from a generated grpc file)
    stub_class=PingServiceStub,
    # Method to call when this DAG is triggered
    call_func='ping',
    # Custom data sent to the "ping" method (can be the request, or grpc metadata)
    data={'request': PingRequest()},
    # Handler called on responses
    response_callback=response_handler,
    streaming=False,
)