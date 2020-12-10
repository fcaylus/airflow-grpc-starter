#!/usr/bin/env sh

mkdir -p build/proto
python -m grpc_tools.protoc -I./ --python_out=build --grpc_python_out=build ./proto/ping.proto
cp -r build/proto src/dags/
cp -r build/proto server
