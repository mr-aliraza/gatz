import json
from json import JSONDecodeError
import grpc
import requests
import re
from google.protobuf.json_format import MessageToDict

from django.http import HttpResponse, JsonResponse
from django.core import serializers
from rest_framework.decorators import api_view
from services.protos.user import user_pb2, user_pb2_grpc


@api_view(["GET"])
def get_user(request):
    response = {}
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
            response = MessageToDict(user)
            # print(response)
            # response = json.loads(response)
            # response = json.dumps(response)
    return JsonResponse(response)


@api_view(["POST"])
def get_token(request):
    try:
        payload = json.loads(request.body)
    except JSONDecodeError:
        payload = {}
    response = requests.post("http://localhost:8001/auth/token/?format=json", data=payload).json()
    return HttpResponse(
        json.dumps(response),
        content_type="application/json"
    )


@api_view(["POST"])
def refresh_token(request):
    try:
        payload = json.loads(request.body)
    except JSONDecodeError:
        payload = {}
    response = requests.post("http://localhost:8001/auth/token/refresh/?format=json", data=payload).json()
    return HttpResponse(
        json.dumps(response),
        content_type="application/json"
    )


@api_view(["POST"])
def create_user(request):
    try:
        payload = json.loads(request.body)
    except JSONDecodeError:
        payload = {}
    response = requests.post("http://localhost:8001/user/register/?format=json", data=payload).json()
    return HttpResponse(
        json.dumps(response),
        content_type="application/json"
    )
