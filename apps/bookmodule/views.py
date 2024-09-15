# apps/bookmodule/views.py

from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    name = request.GET.get("name") or "world!"
    return HttpResponse("Hello, " + name)

def index2(request, val1, val2):
    return HttpResponse(f"value1 = {val1} and value2 = {val2}")
