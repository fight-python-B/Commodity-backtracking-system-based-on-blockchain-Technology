from distutils.command import register

from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from miaTest import models
def hello(request):
  context          = {}
  context['hello'] = 'Hello World!'
  return render(request, 'hello.html', context)

def insert(request):
    if request.method == "POST":
        deliverno = request.POST.get("deliverno", None)
        twz = models.deliver.objects.create(deliverno=deliverno)
        twz.save()
    return render(request,'insert.html')

def goto(request):
    return render(request, 'insert.html', {'articles': 18})

def back(request):
    return render(request,'hello.html', {'articles': 18})

def insert2(request):
    if request.method == "POST":
        inforno = request.POST.get("inforno", None)
        information = request.POST.get("information", None)
        delivery = request.POST.get("delivery", None)
        retailer = request.POST.get("retailer", None)
        twz = models.infor.objects.create(inforno=inforno,information=information,delivery=delivery,retailer=retailer)
        twz.save()
    return render(request,'insert2.html')

def goto2(request):
    return render(request, 'insert2.html', {'articles': 18})

def insert3(request):
    if request.method == "POST":
        orderno = request.POST.get("orderno", None)
        retailer = request.POST.get("retailer", None)
        date = request.POST.get("date", None)
        goods = request.POST.get("goods", None)
        number = request.POST.get("number", None)
        twz = models.order.objects.create(orderno=orderno,retailer=retailer,date=date,goods=goods,number=number)
        twz.save()
    return render(request,'insert3.html')

def show(request):
    people_list = models.order.objects.all()
    return render(request, 'show.html', {"people_list":people_list})

def goto3(request):
    people_list = models.order.objects.all()
    return render(request, 'show.html', {"people_list":people_list})

def del_classes(request):
    nid = request.GET.get('nid')
    models.WordList.objects.filter(id=nid).delete()
    return redirect('/get_classes.html')

def goto4(request):
    people_list = models.infor.objects.all()
    return render(request, 'show2.html', {"people_list":people_list})

def show2(request):
    people_list = models.infor.objects.all()
    return render(request, 'show2.html', {"people_list":people_list})