"""HelloWorld URL Configuration

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
from . import view
from django.conf.urls import url
from django.urls import path

from . import view, test_db

urlpatterns = [
    path('runoob/', view.runoob),
    path('testdb/', test_db.testdb),
    path('search-form/',view.search_form),
    # path('search/',view.search),
    path('search/',test_db.testdb),
]
# urlpatterns1 = [
#     # url(r'^admin/', admin.site.urls),
#    path('runoob/', view.runoob1),
#    # path('runoob/',view.)
#    # path('runoob/',view)
# ]
