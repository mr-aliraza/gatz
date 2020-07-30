from services.protos.category import category_pb2_grpc
from . import models

class CategoryMapping(ProtoMapping):
    # the destination type, must come from a *_pb2.py file compiled from your *.proto file

    __proto__ = domain_pb2.Category

    # the base type of your sqlalchemy types
    __source_input_type__ = models.Base

    id = ProtoKey('id', str)
    name = ProtoKey('name', str)
    description = ProtoKey('description', str)


class business_logic:
    """isolates SQL queries returning objects
    ready for the protobuf serialization layer"""

    @staticmethod
    def get_user_by_uuid(uuid):
        result = models.session.query(models.Category).where(models.Category.uuid==uuid)
        return result.one()


class CategoryService(category_pb2_grpc.CategoryService):
    def GetCategory(self, request, context):
        # retrieve sqlalchemy instance of user by uuid
        user = business_logic.get_user_by_id(request.user_uuid)

        return CategoryMapping(user).to_protobuf()

# https://mercator.readthedocs.io/en/latest/sqlalchemy-orm-support.html