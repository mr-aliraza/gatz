import json
from json import JSONDecodeError
import grpc
import requests
import re
from google.protobuf.json_format import MessageToDict
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import status as response_status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from services.protos.category import category_pb2, category_pb2_grpc
from .utils import get_child_categories
from .category_client import CategoryClient

# Create your views here.
client = CategoryClient()


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def categories(request):
    if request.method == 'POST':
        response = {
            "status": response_status.HTTP_400_BAD_REQUEST,
            "result": "failed",
            "message": "Invalid request"
        }
        try:
            category_data = json.loads(request.body)
        except JSONDecodeError:
            return Response(response, status=response_status.HTTP_400_BAD_REQUEST)
        if category_data['name'] == '' or category_data['name'] is None:
            response = {
                "status": response_status.HTTP_400_BAD_REQUEST,
                "result": "failed",
                "message": "Name is required!"
            }
            return Response(response, status=response_status.HTTP_400_BAD_REQUEST)
        response = client.create_category(request.user.id, category_data)
        return Response(response, status=response["status"])
    else:
        response = {
            "status": response_status.HTTP_400_BAD_REQUEST,
            "result": "failed",
            "message": "Invalid request!"
        }
        try:
            nested = json.loads(request.GET.get('nested', "false"))
        except JSONDecodeError:
            return Response(response, status=response_status.HTTP_400_BAD_REQUEST)
        if nested is not True and nested is not False:
            return Response(response, status=response_status.HTTP_400_BAD_REQUEST)
        elif nested is True:
            response = client.get_categories_list()
        else:
            response = client.get_categories()
        return Response(response)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def categories_detail(request, id):
    if request.method == 'PUT':
        response = {
            "status": response_status.HTTP_400_BAD_REQUEST,
            "result": "failed",
            "message": "Invalid request"
        }
        try:
            category_data = json.loads(request.body)
        except JSONDecodeError:
            return Response(response, status=response_status.HTTP_400_BAD_REQUEST)
        if category_data['name'] == '' or category_data['name'] is None:
            response = {
                "status": response_status.HTTP_400_BAD_REQUEST,
                "result": "failed",
                "message": "Name is required!"
            }
            return Response(response, status=response_status.HTTP_400_BAD_REQUEST)
        response = client.update_category(id, request.user.id, category_data)
        return Response(response, status=response["status"])
    elif request.method == 'DELETE':
        response = {
            "status": response_status.HTTP_400_BAD_REQUEST,
            "result": "failed",
            "message": "Invalid request"
        }
        response = client.del_category(id, request.user.id)
        return Response(response, status=response["status"])
    else:
        response = client.get_category(id)
        return Response(response)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_category(request, id):
    response = []
    # with grpc.insecure_channel('localhost:50052') as channel:
    #     stub = category_pb2_grpc.CategoryControllerStub(channel)
    #     category = stub.Retrieve(category_pb2.CategoryRetrieveRequest(id=id))
    #     response = client.get_category(id)
    response = client.get_category(id)
    return JsonResponse(response)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_category(request, id):
    response = {
        "status": response_status.HTTP_400_BAD_REQUEST,
        "result": "failed",
        "message": "Invalid request"
    }
    try:
        category_data = json.loads(request.body)
    except JSONDecodeError:
        return Response(response, status=response_status.HTTP_400_BAD_REQUEST)
    if category_data['name'] == '' or category_data['name'] is None:
        response = {
            "status": response_status.HTTP_400_BAD_REQUEST,
            "result": "failed",
            "message": "Name is required!"
        }
        return Response(response, status=response_status.HTTP_400_BAD_REQUEST)
    # with grpc.insecure_channel('localhost:50052') as channel:
    #     stub = category_pb2_grpc.CategoryControllerStub(channel)
    #     category = category_pb2.Category(id=category_data['id'], name=category_data['name'].strip(), user_id=request.user.id,
    #                                      description=category_data['description'].strip(), parent_id=category_data['parentId'])
    #     category = stub.Update(category)
    #     response = MessageToDict(category)
    response = client.update_category(id, request.user.id, category_data)
    return Response(response, status=response["status"])


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def del_category(request, id):
    response = {
        "status": response_status.HTTP_400_BAD_REQUEST,
        "result": "failed",
        "message": "Invalid request"
    }
    # with grpc.insecure_channel('localhost:50052') as channel:
    #     stub = category_pb2_grpc.CategoryControllerStub(channel)
    #     category = stub.Destroy(category_pb2.CategoryDeleteRequest(id=id, user_id=request.user.id))
    #     response = MessageToDict(category)
    response = client.del_category(id, request.user.id)
    return Response(response, status=response["status"])


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_category(request):
    response = {
        "status": response_status.HTTP_400_BAD_REQUEST,
        "result": "failed",
        "message": "Invalid request"
    }
    try:
        category_data = json.loads(request.body)
    except JSONDecodeError:
        return Response(response, status=response_status.HTTP_400_BAD_REQUEST)
    if category_data['name'] == '' or category_data['name'] is None:
        response = {
            "status": response_status.HTTP_400_BAD_REQUEST,
            "result": "failed",
            "message": "Name is required!"
        }
        return Response(response, status=response_status.HTTP_400_BAD_REQUEST)
    # with grpc.insecure_channel('localhost:50052') as channel:
    #     stub = category_pb2_grpc.CategoryControllerStub(channel)
    #     category = category_pb2.Category(name=category_data['name'].strip(), user_id=request.user.id,
    #                                      description=category_data['description'].strip(), parent_id=category_data['parentId'])
    #     category = stub.Create(category)
    #     response = MessageToDict(category)
    response = client.create_category(request.user.id, category_data)
    return Response(response, status=response["status"])


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_categories(request):
    response = []
    # with grpc.insecure_channel('localhost:50052') as channel:
    #     stub = category_pb2_grpc.CategoryControllerStub(channel)
    #     category_list = stub.List(category_pb2.CategoryListRequest())
    #     # result = MessageToDict(user_list._response_deserializer)
    #     # result = user_list.__dict__
    #     # print(user_list.response_data)
    #     for category in category_list:
    #         # print(MessageToDict(user))
    #         # response = str(user).replace("\n", ", ")
    #         # response = response.replace("\\", "")
    #         category_data = MessageToDict(category)
    #         response.append(category_data)
    #         # print(response)
    #         # response = json.loads(response)
    #         # response = json.dumps(response)
    response = client.get_categories()
    return JsonResponse(response, safe=False)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_categories_list(request):
    response = []
    # with grpc.insecure_channel('localhost:50052') as channel:
    #     stub = category_pb2_grpc.CategoryControllerStub(channel)
    #     category_list = stub.RetrieveParents(category_pb2.CategoryListRequest())
    #     for category in category_list:
    #         category_data = MessageToDict(category)
    #         category_data['parentId'] = None
    #         # category_childs_list = stub.RetrieveChilds(category_pb2.CategoryRetrieveRequest(id=category_data["id"]))
    #         category_data['nodes'] = get_child_categories(stub, category_data["id"])
    #         # for category_child in category_childs_list:
    #         #     child = MessageToDict(category_child)
    #         #     if child['parentId'] == "None":
    #         #         child['parentId'] = None
    #         #     category_data['childs'].append(child)
    #         response.append(category_data)
    # # return JsonResponse(response, safe=False)
    response = client.get_categories_list()
    return Response(response)