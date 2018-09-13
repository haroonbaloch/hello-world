from django.shortcuts import render
from django.http import HttpResponse
from app2.models import AccessRecord,Topic,Webpage
# Create your views here.


def index2(anyname):
    return HttpResponse("my 2nd rpoject")


#def index3(request):

#    dict = {'templatetag':"now its working here too55"}

#    return render(request,'html/index.html',context=dict)

def index(rocky):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record':webpage_list}
    return render(rocky,'html/index.html',context=date_dict)
