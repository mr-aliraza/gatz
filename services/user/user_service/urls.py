from django.urls import re_path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    re_path(r'^auth/token/$', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^auth/token/refresh/$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^user/register/$', views.UserCreate.as_view(), name='register'),
]
