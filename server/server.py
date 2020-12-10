import grpc
from concurrent import futures
from proto.ping_pb2_grpc import PingServiceServicer, add_PingServiceServicer_to_server
from proto.ping_pb2 import PingResponse


class Server(PingServiceServicer):
    def __init__(self, *args, **kwargs):
        pass

    def ping(self, request, context):
        print('pong')
        result = {'response': 'pong'}
        return PingResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_PingServiceServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:3170')
    server.start()
    print('Ping server started on localhost:3170')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
