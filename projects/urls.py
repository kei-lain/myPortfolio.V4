from django.contrib import admin
from django.urls import path, include , reverse_lazy
from .api import api


urlpatterns = [
    path('api/',(api.urls))
]

