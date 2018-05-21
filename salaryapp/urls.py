from django.conf.urls import url, include
from django.contrib import admin
from salaryapp import views

urlpatterns = [
    url(r'^home/$', views.Home, name='home'),
    url(r'^home/grapha/$', views.GraphA, name='grapha'),
    url(r'^home/graphb/$', views.GraphB, name='graphb'),
    url(r'^home/loaddata/$', views.LoadData.as_view(), name='loaddata'),
]