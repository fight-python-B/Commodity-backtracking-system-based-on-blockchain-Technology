# coding=utf-8
from django.conf.urls import url
from wuliu import views
from django.contrib import admin

urlpatterns = [

    url(r'^wuliu/$', views.add()),
    url(r'^show/$', views.list),
    url('admin/', admin.site.urls),
]
