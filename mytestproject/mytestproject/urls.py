from django.contrib import admin
from django.urls import path
from app2 import views
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    url(r'^d',views.index2,name='index2'),
    url(r'^hi2/', include('app2.urls')),
    path('admin/', admin.site.urls),
]
