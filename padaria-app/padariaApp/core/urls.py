# coding=utf-8

from django.urls import path, re_path
from .views import HomeView, product_list, category, product

app_name = 'core'

urlpatterns = [   
    path('', HomeView.as_view(), name='index'),
    re_path(r'^produtos$', product_list, name='product_list'),
    re_path(r'^(?P<slug>[\w_-]+)/$', category, name='category'),
    re_path(r'^produtos/(?P<slug>[\w_-]+)/$', product, name='product'),
]