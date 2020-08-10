from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^variants/$', views.variants, name='variants'),
    re_path(r'^variants/(?P<id>[0-9a-f-]+)/', views.variants_detail, name='variants_detail'),
    re_path(r'^variant-options/$', views.options, name='options'),
    re_path(r'^variant-options/(?P<id>[0-9a-f-]+)/', views.options_detail, name='options_detail')
]
