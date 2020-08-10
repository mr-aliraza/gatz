from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^attributes/$', views.attributes, name='attributes'),
    re_path(r'^attributes/(?P<id>[0-9a-f-]+)/', views.attributes_detail, name='attributes_detail'),
    re_path(r'^attribute-options/$', views.options, name='options'),
    re_path(r'^attribute-options/(?P<id>[0-9a-f-]+)/', views.options_detail, name='options_detail')
]
