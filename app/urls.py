
from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('role/', views.MyUser.as_view(), name="role")
]
