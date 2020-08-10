import grpc
from services.protos.variant import variant_pb2 as pb2
from services.protos.variant import variant_pb2_grpc as pb2_grpc
from google.protobuf.json_format import MessageToDict
import re


class VariantClient(object):
    """
    Client for accessing the gRPC functionality
    """

    def __init__(self):
        # configure the host and the
        # the port to which the client should connect
        # to.
        self.host = 'localhost'
        self.server_port = 50054

        # instantiate a communication channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client to the server channel
        self.stub = pb2_grpc.VariantControllerStub(self.channel)

    def get_variant(self, id):
        variant = self.stub.Retrieve(pb2.VariantRetrieveRequest(id=id))
        response = MessageToDict(variant)
        return response


    def update_variant(self, id, user_id, variant_data):
        variant = pb2.Variant(id=id, name=variant_data['name'].strip(), user_id=user_id,
                                        description=variant_data['description'].strip())
        variant = self.stub.Update(variant)
        response = MessageToDict(variant)
        return response


    def del_variant(self, id, user_id):
        variant = self.stub.Destroy(pb2.VariantDeleteRequest(id=id, user_id=user_id))
        response = MessageToDict(variant)
        return response


    def create_variant(self, user_id, variant_data):
        variant = pb2.Variant(name=variant_data['name'].strip(), user_id=user_id,
                                        description=variant_data['description'].strip())
        variant = self.stub.Create(variant)
        response = MessageToDict(variant)
        return response


    def get_variants(self):
        response = []
        variant_list = self.stub.List(pb2.VariantListRequest())
        for variant in variant_list:
            variant_data = MessageToDict(variant)
            response.append(variant_data)
        return response



class VariantOptionClient(object):
    """
    Client for accessing the gRPC functionality
    """

    def __init__(self):
        # configure the host and the
        # the port to which the client should connect
        # to.
        self.host = 'localhost'
        self.server_port = 50054

        # instantiate a communication channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client to the server channel
        self.stub = pb2_grpc.VariantOptionControllerStub(self.channel)

    def get_option(self, id):
        option = self.stub.Retrieve(pb2.VariantOptionRetrieveRequest(id=id))
        response = MessageToDict(option)
        return response


    def update_option(self, id, user_id, option_data):
        option = pb2.VariantOption(id=id, name=option_data['name'].strip(), variant_id=option_data['variantId'], user_id=user_id,
                                        description=option_data['description'].strip())
        option = self.stub.Update(option)
        response = MessageToDict(option)
        return response


    def del_option(self, id, user_id):
        option = self.stub.Destroy(pb2.VariantOptionDeleteRequest(id=id, user_id=user_id))
        response = MessageToDict(option)
        return response


    def create_option(self, user_id, option_data):
        option = pb2.VariantOption(name=option_data['name'].strip(), variant_id=option_data['variantId'], user_id=user_id,
                                        description=option_data['description'].strip())
        option = self.stub.Create(option)
        response = MessageToDict(option)
        return response


    def get_options(self):
        response = []
        option_list = self.stub.List(pb2.OptionListRequest())
        for option in option_list:
            option_data = MessageToDict(option)
            response.append(option_data)
        return response


    def get_variant_options(self, variant_id):
        response = []
        option_list = self.stub.VariantOptionList(pb2.VariantOptionListRequest(variant_id=variant_id))
        for option in option_list:
            option_data = MessageToDict(option)
            response.append(option_data)
        return response
