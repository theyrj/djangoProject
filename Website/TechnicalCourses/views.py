from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def Courses(request):
    return HttpResponse('<h1>this is my home</h1>')
