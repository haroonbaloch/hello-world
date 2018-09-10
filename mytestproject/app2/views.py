from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index2(anyname):
    return HttpResponse("my 2nd rpoject")

def index3(request):
<<<<<<< HEAD
    dict = {'templatetag':"your teasxt gtoces here"}
=======
    dict = {'templatetag':"your teasxfv here"}
>>>>>>> c750f717afa4bb99d1c2e401f87ed126ba5d29c9
    return render(request,'html/index.html',context=dict)
