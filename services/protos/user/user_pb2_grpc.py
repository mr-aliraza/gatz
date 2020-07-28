# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import user_pb2 as user__pb2


class UserControllerStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.List = channel.unary_stream(
            '/user.UserController/List',
            request_serializer=user__pb2.UserListRequest.SerializeToString,
            response_deserializer=user__pb2.User.FromString,
        )
        self.Create = channel.unary_unary(
            '/user.UserController/Create',
            request_serializer=user__pb2.User.SerializeToString,
            response_deserializer=user__pb2.User.FromString,
        )
        self.Retrieve = channel.unary_unary(
            '/user.UserController/Retrieve',
            request_serializer=user__pb2.UserRetrieveRequest.SerializeToString,
            response_deserializer=user__pb2.User.FromString,
        )
        self.Update = channel.unary_unary(
            '/user.UserController/Update',
            request_serializer=user__pb2.User.SerializeToString,
            response_deserializer=user__pb2.User.FromString,
        )
        self.Destroy = channel.unary_unary(
            '/user.UserController/Destroy',
            request_serializer=user__pb2.User.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class UserControllerServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def List(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'List': grpc.unary_stream_rpc_method_handler(
            servicer.List,
            request_deserializer=user__pb2.UserListRequest.FromString,
            response_serializer=user__pb2.User.SerializeToString,
        ),
        'Create': grpc.unary_unary_rpc_method_handler(
            servicer.Create,
            request_deserializer=user__pb2.User.FromString,
            response_serializer=user__pb2.User.SerializeToString,
        ),
        'Retrieve': grpc.unary_unary_rpc_method_handler(
            servicer.Retrieve,
            request_deserializer=user__pb2.UserRetrieveRequest.FromString,
            response_serializer=user__pb2.User.SerializeToString,
        ),
        'Update': grpc.unary_unary_rpc_method_handler(
            servicer.Update,
            request_deserializer=user__pb2.User.FromString,
            response_serializer=user__pb2.User.SerializeToString,
        ),
        'Destroy': grpc.unary_unary_rpc_method_handler(
            servicer.Destroy,
            request_deserializer=user__pb2.User.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'user.UserController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
