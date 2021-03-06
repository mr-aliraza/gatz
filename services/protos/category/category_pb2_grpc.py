# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import category_pb2 as category__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class CategoryControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/user.CategoryController/List',
                request_serializer=category__pb2.CategoryListRequest.SerializeToString,
                response_deserializer=category__pb2.Category.FromString,
                )
        self.Create = channel.unary_unary(
                '/user.CategoryController/Create',
                request_serializer=category__pb2.Category.SerializeToString,
                response_deserializer=category__pb2.Category.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/user.CategoryController/Retrieve',
                request_serializer=category__pb2.CategoryRetrieveRequest.SerializeToString,
                response_deserializer=category__pb2.Category.FromString,
                )
        self.RetrieveParents = channel.unary_stream(
                '/user.CategoryController/RetrieveParents',
                request_serializer=category__pb2.CategoryListRequest.SerializeToString,
                response_deserializer=category__pb2.Category.FromString,
                )
        self.RetrieveChilds = channel.unary_stream(
                '/user.CategoryController/RetrieveChilds',
                request_serializer=category__pb2.CategoryRetrieveRequest.SerializeToString,
                response_deserializer=category__pb2.Category.FromString,
                )
        self.Update = channel.unary_unary(
                '/user.CategoryController/Update',
                request_serializer=category__pb2.Category.SerializeToString,
                response_deserializer=category__pb2.Category.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/user.CategoryController/Destroy',
                request_serializer=category__pb2.CategoryDeleteRequest.SerializeToString,
                response_deserializer=category__pb2.Category.FromString,
                )


class CategoryControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveParents(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveChilds(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CategoryControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=category__pb2.CategoryListRequest.FromString,
                    response_serializer=category__pb2.Category.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=category__pb2.Category.FromString,
                    response_serializer=category__pb2.Category.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=category__pb2.CategoryRetrieveRequest.FromString,
                    response_serializer=category__pb2.Category.SerializeToString,
            ),
            'RetrieveParents': grpc.unary_stream_rpc_method_handler(
                    servicer.RetrieveParents,
                    request_deserializer=category__pb2.CategoryListRequest.FromString,
                    response_serializer=category__pb2.Category.SerializeToString,
            ),
            'RetrieveChilds': grpc.unary_stream_rpc_method_handler(
                    servicer.RetrieveChilds,
                    request_deserializer=category__pb2.CategoryRetrieveRequest.FromString,
                    response_serializer=category__pb2.Category.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=category__pb2.Category.FromString,
                    response_serializer=category__pb2.Category.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=category__pb2.CategoryDeleteRequest.FromString,
                    response_serializer=category__pb2.Category.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.CategoryController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CategoryController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/user.CategoryController/List',
            category__pb2.CategoryListRequest.SerializeToString,
            category__pb2.Category.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.CategoryController/Create',
            category__pb2.Category.SerializeToString,
            category__pb2.Category.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.CategoryController/Retrieve',
            category__pb2.CategoryRetrieveRequest.SerializeToString,
            category__pb2.Category.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrieveParents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/user.CategoryController/RetrieveParents',
            category__pb2.CategoryListRequest.SerializeToString,
            category__pb2.Category.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrieveChilds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/user.CategoryController/RetrieveChilds',
            category__pb2.CategoryRetrieveRequest.SerializeToString,
            category__pb2.Category.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.CategoryController/Update',
            category__pb2.Category.SerializeToString,
            category__pb2.Category.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.CategoryController/Destroy',
            category__pb2.CategoryDeleteRequest.SerializeToString,
            category__pb2.Category.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)


class CategoryAttributeControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/user.CategoryAttributeController/List',
                request_serializer=category__pb2.CategoryAttributeListRequest.SerializeToString,
                response_deserializer=category__pb2.CategoryAttribute.FromString,
                )
        self.Create = channel.unary_unary(
                '/user.CategoryAttributeController/Create',
                request_serializer=category__pb2.CategoryAttribute.SerializeToString,
                response_deserializer=category__pb2.CategoryAttribute.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/user.CategoryAttributeController/Retrieve',
                request_serializer=category__pb2.CategoryAttributeRetrieveRequest.SerializeToString,
                response_deserializer=category__pb2.CategoryAttribute.FromString,
                )
        self.Update = channel.unary_unary(
                '/user.CategoryAttributeController/Update',
                request_serializer=category__pb2.CategoryAttribute.SerializeToString,
                response_deserializer=category__pb2.CategoryAttribute.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/user.CategoryAttributeController/Destroy',
                request_serializer=category__pb2.CategoryAttribute.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class CategoryAttributeControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CategoryAttributeControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=category__pb2.CategoryAttributeListRequest.FromString,
                    response_serializer=category__pb2.CategoryAttribute.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=category__pb2.CategoryAttribute.FromString,
                    response_serializer=category__pb2.CategoryAttribute.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=category__pb2.CategoryAttributeRetrieveRequest.FromString,
                    response_serializer=category__pb2.CategoryAttribute.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=category__pb2.CategoryAttribute.FromString,
                    response_serializer=category__pb2.CategoryAttribute.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=category__pb2.CategoryAttribute.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.CategoryAttributeController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CategoryAttributeController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/user.CategoryAttributeController/List',
            category__pb2.CategoryAttributeListRequest.SerializeToString,
            category__pb2.CategoryAttribute.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.CategoryAttributeController/Create',
            category__pb2.CategoryAttribute.SerializeToString,
            category__pb2.CategoryAttribute.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.CategoryAttributeController/Retrieve',
            category__pb2.CategoryAttributeRetrieveRequest.SerializeToString,
            category__pb2.CategoryAttribute.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.CategoryAttributeController/Update',
            category__pb2.CategoryAttribute.SerializeToString,
            category__pb2.CategoryAttribute.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.CategoryAttributeController/Destroy',
            category__pb2.CategoryAttribute.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)


class CategoryVariantControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/user.CategoryVariantController/List',
                request_serializer=category__pb2.CategoryVariantListRequest.SerializeToString,
                response_deserializer=category__pb2.CategoryVariant.FromString,
                )
        self.Create = channel.unary_unary(
                '/user.CategoryVariantController/Create',
                request_serializer=category__pb2.CategoryVariant.SerializeToString,
                response_deserializer=category__pb2.CategoryVariant.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/user.CategoryVariantController/Retrieve',
                request_serializer=category__pb2.CategoryVariantRetrieveRequest.SerializeToString,
                response_deserializer=category__pb2.CategoryVariant.FromString,
                )
        self.Update = channel.unary_unary(
                '/user.CategoryVariantController/Update',
                request_serializer=category__pb2.CategoryVariant.SerializeToString,
                response_deserializer=category__pb2.CategoryVariant.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/user.CategoryVariantController/Destroy',
                request_serializer=category__pb2.CategoryVariant.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class CategoryVariantControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CategoryVariantControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=category__pb2.CategoryVariantListRequest.FromString,
                    response_serializer=category__pb2.CategoryVariant.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=category__pb2.CategoryVariant.FromString,
                    response_serializer=category__pb2.CategoryVariant.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=category__pb2.CategoryVariantRetrieveRequest.FromString,
                    response_serializer=category__pb2.CategoryVariant.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=category__pb2.CategoryVariant.FromString,
                    response_serializer=category__pb2.CategoryVariant.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=category__pb2.CategoryVariant.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.CategoryVariantController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CategoryVariantController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/user.CategoryVariantController/List',
            category__pb2.CategoryVariantListRequest.SerializeToString,
            category__pb2.CategoryVariant.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.CategoryVariantController/Create',
            category__pb2.CategoryVariant.SerializeToString,
            category__pb2.CategoryVariant.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.CategoryVariantController/Retrieve',
            category__pb2.CategoryVariantRetrieveRequest.SerializeToString,
            category__pb2.CategoryVariant.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.CategoryVariantController/Update',
            category__pb2.CategoryVariant.SerializeToString,
            category__pb2.CategoryVariant.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.CategoryVariantController/Destroy',
            category__pb2.CategoryVariant.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
