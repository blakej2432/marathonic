from django.shortcuts import render

def index(request):
    return render(request, 'profiles/index.html')

def login(request):
    return render(request, 'profiles/login.html')