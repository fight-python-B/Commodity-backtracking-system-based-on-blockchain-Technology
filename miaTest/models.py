#python manage.py makemigrations
#python manage.py migrate
# -*- coding: utf-8 -*-
#订单编号，预定商，预定日期，预定商品，预定数量
#订单编号，商品信息，物流名称，零售商名称
#发送的订单编号
from django.db import models

# Create your models here.
class order(models.Model):
    orderno = models.CharField(max_length=20)
    retailer = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    goods = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    def __str__(self):
        return self.orderno,self.retailer,self.date,self.goods,self.number

class infor(models.Model):
    inforno = models.CharField(max_length=20)
    information = models.CharField(max_length=20)
    delivery = models.CharField(max_length=20)
    retailer = models.CharField(max_length=20)
    def __str__(self):
        return self.inforno,self.information,self.delivery,self.retailer

class deliver(models.Model):
    deliverno = models.CharField(max_length=20)
    def __str__(self):
        return self.deliverno



