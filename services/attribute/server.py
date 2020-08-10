import grpc
from concurrent import futures
import time

import sys

sys.path.append("/home/ali/gatz")

# import the generated classes
from services.protos.attribute import attribute_pb2, attribute_pb2_grpc

# import the original crud.py
import crud

# create a class to define the server functions
# derived from attribute_pb2_grpc.AttributeControllerServicer
class AttributeServicer(attribute_pb2_grpc.AttributeControllerServicer):
    def __init__(self):
        self.db = crud.read_attribute_database()
    # create_attribute is exposed here
    # the request and response are of the data types
    # generated as attribute_pb2.Attribute
    def Create(self, request, context):
        response = attribute_pb2.Attribute()
        response = crud.create_attribute(request.name, request.description, request.user_id)
        return response

    def List(self, request, context):
        self.db = crud.read_attribute_database()
        for attribute in self.db:
            yield attribute

    def Retrieve(self, request, context):
        response = attribute_pb2.Attribute()
        response = crud.get_attribute(request.id)
        return response

    def Update(self, request, context):
        response = attribute_pb2.Attribute()
        response = crud.update_attribute(request.id, request.name, request.description, request.user_id)
        return response

    def Destroy(self, request, context):
        response = attribute_pb2.Attribute()
        response = crud.delete_attribute(request.id, request.user_id)
        return response

# create a class to define the server functions
# derived from attribute_pb2_grpc.AttributeOptionControllerServicer
class AttributeOptionServicer(attribute_pb2_grpc.AttributeOptionControllerServicer):
    def __init__(self):
        self.db = crud.read_options_database()
    # create_option is exposed here
    # the request and response are of the data types
    # generated as attribute_pb2.AttributeOption
    def Create(self, request, context):
        response = attribute_pb2.AttributeOption()
        response = crud.create_option(request.name, request.description, request.attribute_id, request.user_id)
        return response

    def List(self, request, context):
        self.db = crud.read_options_database()
        for option in self.db:
            yield option

    def AttributeOptionList(self, request, context):
        self.db = crud.read_attribute_options_database(request.attribute_id)
        for option in self.db:
            yield option

    def Retrieve(self, request, context):
        response = attribute_pb2.AttributeOption()
        response = crud.get_option(request.id)
        return response

    def Update(self, request, context):
        response = attribute_pb2.AttributeOption()
        response = crud.update_option(request.id, request.name, request.description, request.attribute_id, request.user_id)
        return response

    def Destroy(self, request, context):
        response = attribute_pb2.AttributeOption()
        response = crud.delete_option(request.id, request.user_id)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_AttributeControllerServicer_to_server`
# to add the defined class to the created server
attribute_pb2_grpc.add_AttributeControllerServicer_to_server(
        AttributeServicer(), server)

# use the generated function `add_AttributeOptionControllerServicer_to_server`
# to add the defined class to the created server
attribute_pb2_grpc.add_AttributeOptionControllerServicer_to_server(
        AttributeOptionServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50053.')
server.add_insecure_port('[::]:50053')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
