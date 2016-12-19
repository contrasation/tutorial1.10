# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world! You're at the Polls index")

def hello(request):
    return HttpResponse('Hello')

def hello4(request):
    return HttpResponse('Hello4')