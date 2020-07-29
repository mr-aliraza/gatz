import json
from json import JSONDecodeError
import grpc
import requests
import re
from google.protobuf.json_format import MessageToDict
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from rest_framework import status as response_status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from services.protos.user import user_pb2, user_pb2_grpc


@api_view(["GET"])
def get_user(request, id):
    response = []
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserControllerStub(channel)
        user = stub.Retrieve(user_pb2.UserRetrieveRequest(id=int(id)))
        response = MessageToDict(user)
        del response['password']
        # result = MessageToDict(user_list._response_deserializer)
        # result = user_list.__dict__
        # print(user_list.response_data)
        # for user in user_list:
            # print(MessageToDict(user))
            # response = str(user).replace("\n", ", ")
            # response = response.replace("\\", "")
            # response.append(MessageToDict(user))
            # print(response)
            # response = json.loads(response)
            # response = json.dumps(response)
    return JsonResponse(response)


@api_view(["GET"])
def get_users(request):
    response = []
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserControllerStub(channel)
        user_list = stub.List(user_pb2.UserListRequest())
        # result = MessageToDict(user_list._response_deserializer)
        # result = user_list.__dict__
        # print(user_list.response_data)
        for user in user_list:
            # print(MessageToDict(user))
            # response = str(user).replace("\n", ", ")
            # response = response.replace("\\", "")
            user_data = MessageToDict(user)
            del user_data['password']
            response.append(user_data)
            # print(response)
            # response = json.loads(response)
            # response = json.dumps(response)
    return JsonResponse(response, safe=False)


@api_view(["POST"])
@permission_classes([AllowAny])
def create_user(request):
    response = {
        "message": "Invalid request"
    }
    try:
        user_data = json.loads(request.body)
    except JSONDecodeError:
        return Response(response, status=response_status.HTTP_400_BAD_REQUEST)
    password = make_password(user_data.get('password'))
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserControllerStub(channel)
        user = user_pb2.User(first_name=user_data['first_name'], last_name=user_data['last_name'], mobile=user_data['mobile'], email=user_data['email'],
                             password=password, gender=user_data['gender'], date_of_birth=user_data['date_of_birth'], role=6, is_active=True, status=1)
        user = stub.Create(user)
        response = MessageToDict(user)
        del response['password']
    return JsonResponse(response)


# @api_view(["POST"])
# @permission_classes([AllowAny])
# def get_token(request):
#     try:
#         payload = json.loads(request.body)
#     except JSONDecodeError:
#         payload = {}
#     response = requests.post("http://localhost:8001/auth/token/?format=json", data=payload).json()
#     return HttpResponse(
#         json.dumps(response),
#         content_type="application/json"
#     )


# @api_view(["POST"])
# def refresh_token(request):
#     try:
#         payload = json.loads(request.body)
#     except JSONDecodeError:
#         payload = {}
#     response = requests.post("http://localhost:8001/auth/token/refresh/?format=json", data=payload).json()
#     return HttpResponse(
#         json.dumps(response),
#         content_type="application/json"
#     )


# @api_view(["POST"])
# def create_users(request):
#     try:
#         payload = json.loads(request.body)
#     except JSONDecodeError:
#         payload = {}
#     response = requests.post("http://localhost:8001/user/register/?format=json", data=payload).json()
#     return HttpResponse(
#         json.dumps(response),
#         content_type="application/json"
#     )
