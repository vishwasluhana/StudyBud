from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello, World!')

def room(request, room):
    return HttpResponse("Room")