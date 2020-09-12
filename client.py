import grpc

# import the generated classes
import code_pb2
import code_pb2_grpc



while True:

	n=int(input())
	x=int(input())
	y=int(input())
	z=int(input())

# open a gRPC channel
	channel = grpc.insecure_channel('localhost:50051')
	channel1 = grpc.insecure_channel('localhost:50052')
	channel2 = grpc.insecure_channel('localhost:50053')
	channel3 = grpc.insecure_channel('localhost:50054')
# create a stub (client)
	stub = code_pb2_grpc.CodeStub(channel)
	stub1 = code_pb2_grpc.CodeStub(channel1)
	stub2 = code_pb2_grpc.CodeStub(channel2)
	stub3 = code_pb2_grpc.CodeStub(channel3)
# create a valid request message

	number = code_pb2.Number(value=n)
	number1 = code_pb2.Number(value=x)
	number2 = code_pb2.Number(value=y)
	number3 = code_pb2.Number(value=z)
# make the call
	response = stub.code(number)
	response1 = stub.code(number1)
	response2 = stub.code(number2)
	response3 = stub.code(number3)

# et voilà
	print("inc num of %d is %f\n" %(n,response.value))
	print("inc num of %d is %f\n" %(x,response1.value))
	print("inc num of %d is %f\n" %(y,response2.value))
	print("inc num of %d is %f\n" %(z,response3.value))
	print("Enter next number")