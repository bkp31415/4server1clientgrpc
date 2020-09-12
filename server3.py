import grpc
from concurrent import futures
import time

# import the generated classes
import code_pb2
import code_pb2_grpc

# import the original code.py
import code

# create a class to define the server functions
# derived from calc_pb2_grpc.CalcServicer
class CodeServicer(code_pb2_grpc.CodeServicer):

    # code.avg is exposed here
    # the request and response are of the data types
    # generated as code_pb2.Number
    def code(self, request, context):
        response = code_pb2.Number()
        response.value = code.code(request.value)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_calcServicer_to_server`
# to add the defined class to the created server
code_pb2_grpc.add_CodeServicer_to_server(
        CodeServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50054.')
server.add_insecure_port('[::]:50054')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)