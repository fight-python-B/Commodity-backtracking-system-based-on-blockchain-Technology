from django.test import TestCase

# Create your tests here.
from miaTest.models import order
order.objects.create(orderno='00001',retailer='shopone',date='2020.07.01',goods='thingone',number='100')
order.objects.create(orderno='00002',retailer='shoptwo',date='2020.07.02',goods='thingtwo',number='200')
from miaTest.models import infor
infor.objects.create(inforno='0001',information='v1', delivery='penguin',retailer='shopone')