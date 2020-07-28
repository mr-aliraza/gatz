from .models import User
from .serializers import UsersSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (AllowAny,)
