# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Purchaseorder(models.Model):
    pur_ordernum = models.CharField(max_length=50, blank=True, null=True)
    pur_goodsname = models.CharField(max_length=50, blank=True, null=True)
    pur_quantity = models.IntegerField(blank=True, null=True)
    productname = models.CharField(max_length=50, blank=True, null=True)
    pur_time = models.DateTimeField(blank=True, null=True)
    productad = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'purchaseorder'


class Sellorder(models.Model):
    retailername = models.CharField(max_length=50, blank=True, null=True)
    sell_goodsname = models.CharField(max_length=50, blank=True, null=True)
    sell_quantity = models.IntegerField(blank=True, null=True)
    retailer_ad = models.CharField(max_length=100, blank=True, null=True)
    sell_ordernum = models.CharField(max_length=50, blank=True, null=True)
    sell_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sellorder'


class Stock(models.Model):
    goodsname = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    productname = models.CharField(max_length=50, blank=True, null=True)
    storage = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock'


class Text(models.Model):
    text = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'text'
