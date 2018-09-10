from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(anyname):
    return HttpResponse("my 2nd rpoject")
