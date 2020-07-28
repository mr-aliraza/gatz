from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^users/$', views.get_user, name='token_obtain_pair'),
    re_path(r'^auth/token/$', views.get_token, name='token_obtain_pair'),
    re_path(r'^auth/token/refresh/$', views.refresh_token, name='token_refresh'),
    re_path(r'^user/register/$', views.create_user, name='register'),
]
