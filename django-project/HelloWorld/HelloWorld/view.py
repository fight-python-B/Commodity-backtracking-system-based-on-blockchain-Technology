from django.http import HttpResponse
import datetime
from django.shortcuts import render
from TestModel.models import Test

def search_form(request):
  return render(request,'search_form.html')
# def search(request):
#   if 'q' in request.GET:
#     message = 'You searched for: %r' % request.GET['q']
#   else:
#     message = 'You submitted an empty form.'
#   return HttpResponse(message)
# def search(request):
#   if 'q' in request.GET and request.GET['q']:
#     q = request.GET['q']
#     # products = Test.objects.filter(name__icontains=q)
#
#     products = Test.objects.filter(id=q)
#     productNumber=products.name
#     return render(request,'search_results.html',
#       {'products': products, 'query': q ,'productNumber':productNumber})
#   else:
#     return HttpResponse('Please submit a search term.')
# def runoob(request):
#     context          = {}
#     context['hello'] = 'Hello World!'
#     return render(request, 'runoob.html', context)
# def hello(request):
#     return HttpResponse("Hello world ! ")
# def sayHello(request):
#     s = 'Hello World!'
#     current_time = datetime.datetime.now()
#     html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
#     return HttpResponse(html)
#测试
def num(request):
    x="0x11111111111"
    return render(request,'runooob.html',{"x": x})
def runoob(request):
    productNumber ="0x11111111111"
    reserveNumber="Ex11111111111"
    productCompany="没有想到公司"
    startTime="20200102"
    middleCompany="还没想到公司"
    TransforTime="20200102"
    endCompany="不想了公司"
    saleTime="20200102"
    return render(request, "runoob.html", {"productNumber": productNumber,"reserveNumber":reserveNumber,"productCompany":productCompany,"startTime":startTime,"middleCompany":middleCompany,"TransforTime":TransforTime,"endCompany":endCompany,"saleTime":saleTime})
def runoob1(request):
    name ="Ex11111111111"
    return render(request, "runoob.html", {"name1": name})
