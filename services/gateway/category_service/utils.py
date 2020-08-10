from services.protos.category import category_pb2
from google.protobuf.json_format import MessageToDict


def get_child_categories(stub, id):
    category_childs_list = stub.RetrieveChilds(category_pb2.CategoryRetrieveRequest(id=id))
    childs = []
    for category_child in category_childs_list:
        child = MessageToDict(category_child)
        child['nodes'] = get_child_categories(stub, child["id"])
        childs.append(child)
    return childs