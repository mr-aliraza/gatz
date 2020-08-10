from django.urls import re_path

from . import views

urlpatterns = [
    # re_path(r'^category/create$', views.create_category, name='create_category'),
    # re_path(r'^category/list$', views.get_categories, name='get_categories'),
    # re_path(r'^category/nested-list$', views.get_categories_list, name='get_categories_list'),
    # re_path(r'^category/(?P<id>[0-9a-f-]+)/get$', views.get_category, name='get_category'),
    # re_path(r'^category/(?P<id>[0-9a-f-]+)/update$', views.update_category, name='update_category'),
    # re_path(r'^category/(?P<id>[0-9a-f-]+)/delete$', views.del_category, name='del_category'),
    re_path(r'^categories/$', views.categories, name='categories'),
    re_path(r'^categories/(?P<id>[0-9a-f-]+)/', views.categories_detail, name='categories_detail')
]
