import grpc
from services.protos.category import category_pb2 as pb2
from services.protos.category import category_pb2_grpc as pb2_grpc
from google.protobuf.json_format import MessageToDict
from .utils import get_child_categories


class CategoryClient(object):
    """
    Client for accessing the gRPC functionality
    """

    def __init__(self):
        # configure the host and the
        # the port to which the client should connect
        # to.
        self.host = 'localhost'
        self.server_port = 50052

        # instantiate a communication channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client to the server channel
        self.stub = pb2_grpc.CategoryControllerStub(self.channel)

    def get_category(self, id):
        category = self.stub.Retrieve(pb2.CategoryRetrieveRequest(id=id))
        response = MessageToDict(category)
        if response["parentId"] == "None":
            response["parentId"] = None
        if response["parentName"] == "None":
            response["parentName"] = None
        return response


    def update_category(self, id, user_id, category_data):
        category = pb2.Category(id=id, name=category_data['name'].strip(), user_id=user_id,
                                        description=category_data['description'].strip(), parent_id=category_data['parentId'])
        category = self.stub.Update(category)
        response = MessageToDict(category)
        return response


    def del_category(self, id, user_id):
        category = self.stub.Destroy(pb2.CategoryDeleteRequest(id=id, user_id=user_id))
        response = MessageToDict(category)
        return response


    def create_category(self, user_id, category_data):
        category = pb2.Category(name=category_data['name'].strip(), user_id=user_id,
                                        description=category_data['description'].strip(), parent_id=category_data['parentId'])
        category = self.stub.Create(category)
        response = MessageToDict(category)
        return response


    def get_categories(self):
        response = []
        category_list = self.stub.List(pb2.CategoryListRequest())
        for category in category_list:
            category_data = MessageToDict(category)
            if category_data["parentId"] == "None":
                category_data["parentId"] = None
            if category_data["parentName"] == "None":
                category_data["parentName"] = None
            response.append(category_data)
        return response


    def get_categories_list(self):
        response = []
        category_list = self.stub.RetrieveParents(pb2.CategoryListRequest())
        for category in category_list:
            category_data = MessageToDict(category)
            category_data['parentId'] = None
            category_data['nodes'] = get_child_categories(self.stub, category_data["id"])
            response.append(category_data)
        return response