# coding=utf-8

from django.urls import path, re_path
from .views import HomeView

app_name = 'core'

urlpatterns = [   
    path('', HomeView.as_view(), name='index'),
]