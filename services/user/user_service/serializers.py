from .models import User
from django.contrib.auth import password_validation
from django.core.validators import RegexValidator
from rest_framework import serializers, exceptions
from django_grpc_framework import proto_serializers
from services.protos.user import user_pb2


alphabets = RegexValidator(r'^[a-zA-Z ]*$', 'Only alphabets allowed in name!')
numeric = RegexValidator(r'^[0-9]*$', 'Enter a valid mobile number!')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'mobile')


class UsersSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=30, required=True,
                                       error_messages={'max_length': 'First Name is too long!',
                                                       'required': 'First Name is required!'}, validators=[alphabets])
    last_name = serializers.CharField(max_length=255, required=True,
                                      error_messages={'max_length': 'Last Name is too long!',
                                                      'required': 'Last Name is required!'}, validators=[alphabets])
    email = serializers.EmailField(max_length=255, required=True, error_messages={'max_length': 'Email is too long!',
                                                                                  'required': 'Email is required!'})
    mobile = serializers.CharField(required=True, allow_null=True, max_length=25, validators=[numeric])

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'mobile', 'email', 'password', 'gender')
        extra_kwargs = {'password': {'write_only': True}, 'mobile': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return UserSerializer(user, many=False).data

    def validate_password(self, value):
        """
        Check that the blog post is about Django.
        """
        # get the password from the data
        password = value

        errors = dict()
        try:
            # validate the password and catch the exception
            password_validation.validate_password(password=password)

        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)
        return value


class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = User
        proto_class = user_pb2.User
        fields = ['id', 'first_name', 'last_name', 'email', 'mobile', 'gender', 'date_of_birth', 'is_active', 'status',
                  'role']
