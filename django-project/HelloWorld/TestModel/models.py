from django.db import models

# Create your models here.
from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=20)
    productNumber=models.CharField(max_length=20)
    producerName=models.CharField(max_length=20)
    StartTime=models.CharField(max_length=20)
    TransforName=models.CharField(max_length=20)
    TransforTime=models.CharField(max_length=20)
    SaleName=models.CharField(max_length=20)
    SaleTime=models.CharField(max_length=20)