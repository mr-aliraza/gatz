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
from services.protos.attribute import attribute_pb2, attribute_pb2_grpc
from .attribute_client import AttributeClient, AttributeOptionClient

# Create your views here.
client = AttributeClient()
options_client = AttributeOptionClient()


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def attributes(request):
    if request.method == 'POST':
        response = {
            "status": response_status.HTTP_400_BAD_REQUEST,
            "result": "failed",
            "message": "Invalid request"
        }
        try:
            attribute_data = json.loads(request.body)
        except JSONDecodeError:
            return Response(response, status=response_status.HTTP_400_BAD_REQUEST)
        if attribute_data['name'] == '' or attribute_data['name'] is None:
            response = {
                "status": response_status.HTTP_400_BAD_REQUEST,
                "result": "failed",
                "message": "Name is required!"
            }
            return Response(response, status=response_status.HTTP_400_BAD_REQUEST)
        response = client.create_attribute(request.user.id, attribute_data)
        return Response(response, status=response["status"])
    else:
        response = {
            "status": response_status.HTTP_400_BAD_REQUEST,
            "result": "failed",
            "message": "Invalid request!"
        }
        response = client.get_attributes()
        return Response(response)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def attributes_detail(request, id):
    if request.method == 'PUT':
        response = {
            "status": response_status.HTTP_400_BAD_REQUEST,
            "result": "failed",
            "message": "Invalid request"
        }
        try:
            attribute_data = json.loads(request.body)
        except JSONDecodeError:
            return Response(response, status=response_status.HTTP_400_BAD_REQUEST)
        if attribute_data['name'] == '' or attribute_data['name'] is None:
            response = {
                "status": response_status.HTTP_400_BAD_REQUEST,
                "result": "failed",
                "message": "Name is required!"
            }
            return Response(response, status=response_status.HTTP_400_BAD_REQUEST)
        response = client.update_attribute(id, request.user.id, attribute_data)
        return Response(response, status=response["status"])
    elif request.method == 'DELETE':
        response = {
            "status": response_status.HTTP_400_BAD_REQUEST,
            "result": "failed",
            "message": "Invalid request"
        }
        response = client.del_attribute(id, request.user.id)
        return Response(response, status=response["status"])
    else:
        response = client.get_attribute(id)
        return Response(response)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def options(request):
    if request.method == 'POST':
        response = {
            "status": response_status.HTTP_400_BAD_REQUEST,
            "result": "failed",
            "message": "Invalid request"
        }
        try:
            options_data = json.loads(request.body)
        except JSONDecodeError:
            return Response(response, status=response_status.HTTP_400_BAD_REQUEST)
        if options_data['name'] == '' or options_data['name'] is None:
            response = {
                "status": response_status.HTTP_400_BAD_REQUEST,
                "result": "failed",
                "message": "Name is required!"
            }
            return Response(response, status=response_status.HTTP_400_BAD_REQUEST)
        response = options_client.create_option(request.user.id, options_data)
        return Response(response, status=response["status"])
    else:
        response = {
            "status": response_status.HTTP_400_BAD_REQUEST,
            "result": "failed",
            "message": "Invalid request!"
        }
        try:
            attribute_id = request.GET.get('attributeId', None)
        except:
            return Response(response, status=response_status.HTTP_400_BAD_REQUEST)
        if attribute_id:
            pattern = re.compile("^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}")
            if pattern.match(attribute_id):
                response = options_client.get_attribute_options(attribute_id)
            else:
                response = {
                    "status": response_status.HTTP_400_BAD_REQUEST,
                    "result": "failed",
                    "message": "Invalid attribute id!"
                }
        else:
            response = options_client.get_options()
        return Response(response)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def options_detail(request, id):
    if request.method == 'PUT':
        response = {
            "status": response_status.HTTP_400_BAD_REQUEST,
            "result": "failed",
            "message": "Invalid request"
        }
        try:
            options_data = json.loads(request.body)
        except JSONDecodeError:
            return Response(response, status=response_status.HTTP_400_BAD_REQUEST)
        if options_data['name'] == '' or options_data['name'] is None:
            response = {
                "status": response_status.HTTP_400_BAD_REQUEST,
                "result": "failed",
                "message": "Name is required!"
            }
            return Response(response, status=response_status.HTTP_400_BAD_REQUEST)
        response = options_client.update_option(id, request.user.id, options_data)
        return Response(response, status=response["status"])
    elif request.method == 'DELETE':
        response = {
            "status": response_status.HTTP_400_BAD_REQUEST,
            "result": "failed",
            "message": "Invalid request"
        }
        response = options_client.del_option(id, request.user.id)
        return Response(response, status=response["status"])
    else:
        response = options_client.get_option(id)
        return Response(response)
