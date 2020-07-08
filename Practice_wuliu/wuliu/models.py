from django.db import models
class wuliu(models.Model):
    num1 = models.CharField(max_length=10,unique=True)
    num2 = models.CharField(max_length=10,unique=True)
    product_name = models.CharField(max_length=1000,default="")
    product_address = models.CharField(max_length=1000,default="")
    product_time = models.CharField(max_length=1000,default="")
    logistics_name = models.CharField(max_length=1000,default="")
    logistics_address = models.CharField(max_length=1000,default="")
    logistics_time = models.CharField(max_length=1000,default="")
    sale_name = models.CharField(max_length=1000,default="")
    sale_address = models.CharField(max_length=1000,default="")
    sale_time = models.CharField(max_length=1000,default="")
    information= models.CharField(max_length=10000,default="")
# Create your models here.
