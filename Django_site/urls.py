
from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('', include('lab4.urls')),
]

