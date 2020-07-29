from django.urls import re_path
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    # re_path(r'^users$', views.get_users, name='get_users'),
    re_path(r'^user/(?P<id>\d+)/get$', views.get_user, name='get_user'),
    re_path(r'^user/create$', views.create_user, name='create_user'),
    re_path(r'^auth/token/$', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^auth/token/refresh/$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # re_path(r'^auth/token/$', views.get_token, name='token_obtain_pair'),
    # re_path(r'^auth/token/refresh/$', views.refresh_token, name='token_refresh'),
    # re_path(r'^user/register/$', views.create_user, name='register'),
]
