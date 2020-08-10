import grpc
from concurrent import futures
import time

import sys

sys.path.append("/home/ali/gatz")

# import the generated classes
from services.protos.category import category_pb2, category_pb2_grpc

# import the original crud.py
import crud

# create a class to define the server functions
# derived from category_pb2_grpc.CategoryControllerServicer
class CategoryServicer(category_pb2_grpc.CategoryControllerServicer):
    def __init__(self):
        self.db = crud.read_category_database()
    # create_category is exposed here
    # the request and response are of the data types
    # generated as category_pb2.Category
    def Create(self, request, context):
        response = category_pb2.Category()
        response = crud.create_category(request.parent_id, request.name, request.description, request.user_id)
        return response

    def List(self, request, context):
        self.db = crud.read_category_database()
        for category in self.db:
            yield category

    def Retrieve(self, request, context):
        response = category_pb2.Category()
        response = crud.get_category(request.id)
        return response

    def RetrieveParents(self, request, context):
        categories = crud.get_category_parents()
        for category in categories:
            yield category

    def RetrieveChilds(self, request, context):
        categories = crud.get_category_childs(request.id)
        for category in categories:
            yield category

    def Update(self, request, context):
        response = category_pb2.Category()
        response = crud.update_category(request.id, request.name, request.description, request.parent_id, request.user_id)
        return response

    def Destroy(self, request, context):
        response = category_pb2.Category()
        response = crud.delete_category(request.id, request.user_id)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CategoryControllerServicer_to_server`
# to add the defined class to the created server
category_pb2_grpc.add_CategoryControllerServicer_to_server(
        CategoryServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50052.')
server.add_insecure_port('[::]:50052')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
