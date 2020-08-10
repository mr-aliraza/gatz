import grpc
from concurrent import futures
import time

import sys

sys.path.append("/home/ali/gatz")

# import the generated classes
from services.protos.variant import variant_pb2, variant_pb2_grpc

# import the original crud.py
import crud

# create a class to define the server functions
# derived from variant_pb2_grpc.VariantControllerServicer
class VariantServicer(variant_pb2_grpc.VariantControllerServicer):
    def __init__(self):
        self.db = crud.read_variant_database()
    # create_variant is exposed here
    # the request and response are of the data types
    # generated as variant_pb2.Variant
    def Create(self, request, context):
        response = variant_pb2.Variant()
        response = crud.create_variant(request.name, request.description, request.user_id)
        return response

    def List(self, request, context):
        self.db = crud.read_variant_database()
        for variant in self.db:
            yield variant

    def Retrieve(self, request, context):
        response = variant_pb2.Variant()
        response = crud.get_variant(request.id)
        return response

    def Update(self, request, context):
        response = variant_pb2.Variant()
        response = crud.update_variant(request.id, request.name, request.description, request.user_id)
        return response

    def Destroy(self, request, context):
        response = variant_pb2.Variant()
        response = crud.delete_variant(request.id, request.user_id)
        return response

# create a class to define the server functions
# derived from variant_pb2_grpc.VariantOptionControllerServicer
class VariantOptionServicer(variant_pb2_grpc.VariantOptionControllerServicer):
    def __init__(self):
        self.db = crud.read_options_database()
    # create_option is exposed here
    # the request and response are of the data types
    # generated as variant_pb2.VariantOption
    def Create(self, request, context):
        response = variant_pb2.VariantOption()
        response = crud.create_option(request.name, request.description, request.variant_id, request.user_id)
        return response

    def List(self, request, context):
        self.db = crud.read_options_database()
        for option in self.db:
            yield option

    def VariantOptionList(self, request, context):
        self.db = crud.read_variant_options_database(request.variant_id)
        for option in self.db:
            yield option

    def Retrieve(self, request, context):
        response = variant_pb2.VariantOption()
        response = crud.get_option(request.id)
        return response

    def Update(self, request, context):
        response = variant_pb2.VariantOption()
        response = crud.update_option(request.id, request.name, request.description, request.variant_id, request.user_id)
        return response

    def Destroy(self, request, context):
        response = variant_pb2.VariantOption()
        response = crud.delete_option(request.id, request.user_id)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_VariantControllerServicer_to_server`
# to add the defined class to the created server
variant_pb2_grpc.add_VariantControllerServicer_to_server(
        VariantServicer(), server)

# use the generated function `add_VariantOptionControllerServicer_to_server`
# to add the defined class to the created server
variant_pb2_grpc.add_VariantOptionControllerServicer_to_server(
        VariantOptionServicer(), server)

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
