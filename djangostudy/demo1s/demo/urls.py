from django.contrib import admin
from django.urls import path
from . import views

app_name = 'demo'

urlpatterns = [
    path('', views.dealer, name='dealer'),
    path('search_storage/', views.search_storage, name='search_storage'),
    path('alter_storage/', views.alter_storage, name='alter_storage'),
    path('alterhandle/', views.alterhandle, name='alterhandle'),
    path('handle/', views.handle, name='handle'),
    path('sell_order/', views.search_order, name='search_order'),
    path('purchase/',views.purchase,name='purchase'),
    path('purhandle/', views.purhandle, name='purhandle'),
    path('pur_order/', views.search_purorder, name='search_purorder'),
]
