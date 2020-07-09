from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import Test

# 数据库操作
# def testdb(request):
#     test1 = Test(name='runoob')
#     test1.save()
#     return HttpResponse("<p>数据添加成功！</p>")
def testdb(request):

    response = ""
    response1 = ""
    response2 = ""
    response3 = ""
    response4 = ""
    response5 = ""
    response6 = ""
    response7 = ""
    response8 = ""

    if 'q' in request.GET and request.GET['q']:
        q=request.GET['q']
        list = Test.objects.filter(name=q)
        for var in list:
            response1 += var.name + " "
            response2 += var.productNumber+ " "
            response3 += var.producerName+ " "
            response4 += var.StartTime+ " "
            response5 += var.TransforName+ " "
            response6 += var.TransforTime+ " "
            response7 += var.SaleName+ " "
            response8 += var.SaleTime+ " "
        # return HttpResponse("<p>" + response + "</p>")
        return render(request,"runoob.html",{"response1":response1, "response2":response2, "response3":response3, "response4":response4, "response5":response5, "response6":response6, "response7":response7, "response8": response8})
    else:
        return HttpResponse('Please submit a search term.')

