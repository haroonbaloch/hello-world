from django.conf.urls import url
from app2 import views

urlpatterns = [

    url(r'^$',views.index2,name='index'),

]
