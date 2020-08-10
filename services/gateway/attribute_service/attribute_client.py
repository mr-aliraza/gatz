import grpc
from services.protos.attribute import attribute_pb2 as pb2
from services.protos.attribute import attribute_pb2_grpc as pb2_grpc
from google.protobuf.json_format import MessageToDict
import re


class AttributeClient(object):
    """
    Client for accessing the gRPC functionality
    """

    def __init__(self):
        # configure the host and the
        # the port to which the client should connect
        # to.
        self.host = 'localhost'
        self.server_port = 50053

        # instantiate a communication channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client to the server channel
        self.stub = pb2_grpc.AttributeControllerStub(self.channel)

    def get_attribute(self, id):
        attribute = self.stub.Retrieve(pb2.AttributeRetrieveRequest(id=id))
        response = MessageToDict(attribute)
        return response


    def update_attribute(self, id, user_id, attribute_data):
        attribute = pb2.Attribute(id=id, name=attribute_data['name'].strip(), user_id=user_id,
                                        description=attribute_data['description'].strip())
        attribute = self.stub.Update(attribute)
        response = MessageToDict(attribute)
        return response


    def del_attribute(self, id, user_id):
        attribute = self.stub.Destroy(pb2.AttributeDeleteRequest(id=id, user_id=user_id))
        response = MessageToDict(attribute)
        return response


    def create_attribute(self, user_id, attribute_data):
        attribute = pb2.Attribute(name=attribute_data['name'].strip(), user_id=user_id,
                                        description=attribute_data['description'].strip())
        attribute = self.stub.Create(attribute)
        response = MessageToDict(attribute)
        return response


    def get_attributes(self):
        response = []
        attribute_list = self.stub.List(pb2.AttributeListRequest())
        for attribute in attribute_list:
            attribute_data = MessageToDict(attribute)
            response.append(attribute_data)
        return response



class AttributeOptionClient(object):
    """
    Client for accessing the gRPC functionality
    """

    def __init__(self):
        # configure the host and the
        # the port to which the client should connect
        # to.
        self.host = 'localhost'
        self.server_port = 50053

        # instantiate a communication channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client to the server channel
        self.stub = pb2_grpc.AttributeOptionControllerStub(self.channel)

    def get_option(self, id):
        option = self.stub.Retrieve(pb2.AttributeOptionRetrieveRequest(id=id))
        response = MessageToDict(option)
        return response


    def update_option(self, id, user_id, option_data):
        option = pb2.AttributeOption(id=id, name=option_data['name'].strip(), attribute_id=option_data['attributeId'], user_id=user_id,
                                        description=option_data['description'].strip())
        option = self.stub.Update(option)
        response = MessageToDict(option)
        return response


    def del_option(self, id, user_id):
        option = self.stub.Destroy(pb2.AttributeOptionDeleteRequest(id=id, user_id=user_id))
        response = MessageToDict(option)
        return response


    def create_option(self, user_id, option_data):
        option = pb2.AttributeOption(name=option_data['name'].strip(), attribute_id=option_data['attributeId'], user_id=user_id,
                                        description=option_data['description'].strip())
        option = self.stub.Create(option)
        response = MessageToDict(option)
        return response


    def get_options(self):
        response = []
        option_list = self.stub.List(pb2.OptionsListRequest())
        for option in option_list:
            option_data = MessageToDict(option)
            response.append(option_data)
        return response


    def get_attribute_options(self, attribute_id):
        response = []
        option_list = self.stub.AttributeOptionList(pb2.AttributeOptionListRequest(attribute_id=attribute_id))
        for option in option_list:
            option_data = MessageToDict(option)
            response.append(option_data)
        return response
