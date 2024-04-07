from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("login",views.login,name="login"),
     path("insert_project",views.insert_project,name="insert_project")

    
]
