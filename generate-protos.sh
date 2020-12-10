#!/usr/bin/env sh
set -e

mkdir -p build/proto
# When generating protobuf files, the python packages will be relative to the -I directory
# In this case, we'll be able to access the files using:
#   import proto.ping_service_pb2
python -m grpc_tools.protoc -I./ --python_out=build --grpc_python_out=build ./proto/ping.proto
cp -r build/proto src/airflow/dags/
cp -r build/proto src/server
