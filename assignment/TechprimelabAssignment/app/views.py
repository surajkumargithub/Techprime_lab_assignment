# File: app/views.py

from django.shortcuts import render

def login(request):
   
    return render(request, 'login.html')

def insert_project(request):
    
    return render(request, 'insert_project.html')

