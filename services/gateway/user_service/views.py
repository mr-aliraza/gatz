import json
from json import JSONDecodeError
import grpc
import requests
import re

from django.http import HttpResponse, JsonResponse
from django.core import serializers
from rest_framework.decorators import api_view
from services.protos.user import user_pb2, user_pb2_grpc


@api_view(["GET"])
def get_user(request):
    response = {}
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserControllerStub(channel)
        for user in stub.List(user_pb2.UserListRequest()):
            response = str(user).replace("\n", ", ")
            response = response.replace("\\", "")
            response = "{" + response[:-2] + "}"
            print(response)
            # response = json.loads(response)
            response = json.dumps(response)
    return HttpResponse(response, content_type="application/json")


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
