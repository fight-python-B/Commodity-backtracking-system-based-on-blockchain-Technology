from django.http import HttpResponse
from django.shortcuts import render
from . import service
from demo.models import Stock, Sellorder, Purchaseorder
from demo import models


# Create your views here.
def dealer(request):
    return render(request, "demo/dealer.html", {})


# 库存查询
def search_storage(request):
    return render(request, "demo/storage.html", {})


def alter_storage(request):
    return render(request, "demo/alterstorage.html", {})


# 库存修改
def alterhandle(request):
    a_goodsname = request.POST['a_goodsname']
    a_quantity = request.POST['a_quantity']
    a_productname = request.POST['a_productname']
    a_storage = request.POST['a_storage']
    t = Stock.objects.get(goodsname=a_goodsname)
    t.quantity = a_quantity
    t.productname = a_productname
    t.storage = a_storage
    t.save()
    return HttpResponse("修改成功")


# 查看销售订单
def search_order(request):
    order_list = models.Sellorder.objects.all()
    return render(request, "demo/sellorder.html", {"order_list": order_list})


# 库存搜索
def handle(request):
    text = request.POST["搜索库存"]
    service.addText(text)
    db = Stock.objects.all()
    po_list = []
    for i in db:
        if text in i.goodsname:
            po_list.append(i.quantity)
    return render(request, "demo/resp.html", {"resp": po_list})


# 添加购买订单
def purchase(request):
    return render(request, "demo/purchase.html", {})


def purhandle(request):
    if request.method == 'POST':
        a_ordernum = request.POST['a_ordernum']
        a_goodsname = request.POST['a_goodsname']
        a_quantity = request.POST['a_quantity']
        a_productname = request.POST['a_productname']
        a_time = request.POST['a_time']
        a_productad = request.POST['a_productad']
        models.Purchaseorder.objects.create(pur_ordernum=a_ordernum,
                                            pur_goodsname=a_goodsname,
                                            pur_quantity=a_quantity,
                                            productname=a_productname,
                                            productad=a_productad,
                                            pur_time=a_time)
    return HttpResponse("提交成功")


# 查看购买订单
def search_purorder(request):
    order_list = models.Purchaseorder.objects.all()
    return render(request, "demo/purorder.html", {"order_list": order_list})
