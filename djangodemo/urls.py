"""djangodemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miaTest import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hello),
    path('insert/',views.insert),
    path('goto/',views.goto,name='goto'),
    path('back/',views.back,name='back'),
    path('insert2/', views.insert2),
    path('goto2/', views.goto2, name='goto2'),
    path('goto3/', views.goto3, name='goto3'),
    path('show/',views.show),
    path('goto4/', views.goto4, name='goto4'),
    path('show2/',views.show2),
]