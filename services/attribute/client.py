import grpc

import sys

sys.path.append("/home/ali/gatz")

# import the generated classes
from services.protos.category import category_pb2, category_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50052')

# create a stub (client)
stub = category_pb2_grpc.CategoryControllerStub(channel)

# create a valid request message
category = category_pb2.Category(name="My Category", description="My Description", parent_id=None)

# make the call
response = stub.Create(category)

# et voilà
print(response)