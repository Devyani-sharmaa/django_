from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("hello world")

def about(request):
    return HttpResponse("<h1> i am devyani</h1>")