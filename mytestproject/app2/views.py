from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index2(anyname):
    return HttpResponse("my 2nd rpoject")

def index3(request):
    dict = {'templatetag':"your haroon here"}
    return render(request,'html/index.html',context=dict)
