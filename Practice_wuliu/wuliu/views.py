from __future__ import unicode_literals
from wuliu import models
from django.shortcuts import render

def add(request):
 if request.method == "POST":
  num1 = request.POST.get('num1', None)
  num2 = request.POST.get('num2', None)
  product_name = request.POST.get('product_name', None)
  product_address = request.POST.get('product_address', None)
  product_time = request.POST.get('product_address', None)
  logistics_name = request.POST.get('logistics_name', None)
  logistics_address = request.POST.get('logistics_address', None)
  logistics_time = request.POST.get('logistics_address', None)
  sale_name = request.POST.get('sale_name', None)
  sale_address = request.POST.get('sale_address', None)
  sale_time = request.POST.get('sale_address', None)
  information = request.POST.get('information', None)
  twz = models.wuliu.objects.create(num1=num1,num2=num2,product_name=product_name,product_address=product_address,product_time=product_time,logistics_name=logistics_name,logistics_address=logistics_address,logistics_time=logistics_time,sale_name=sale_name,sale_address=sale_address,sale_time=sale_time,information=information)
  twz.save()
 return render(request, 'wuliu.html')


def list(request):
 list = models.wuliu.objects.all()
 return render(request, 'show.html', {"list": list})
# def wuliu(request):
#  if request.method == 'GET':
#   return render(request, 'wuliu.html')
#  else:
#   num1 = request.POST.get('num1', '')
#   num2 = request.POST.get('num2', '')
#   product_name = request.POST.get('product_name', '')
#   product_address = request.POST.get('product_address', '')
#   product_time = request.POST.get('product_address', '')
#   logistics_name = request.POST.get('logistics_name', '')
#   logistics_address = request.POST.get('logistics_address', '')
#   logistics_time = request.POST.get('logistics_address', '')
#   sale_name = request.POST.get('sale_name', '')
#   sale_address = request.POST.get('sale_address', '')
#   sale_time = request.POST.get('sale_address', '')
#   information=request.POST.get('information', '')
#  conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="wuliu", charset='utf8')
#  with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
#   cursor.execute("INSERT INTO wuliu_wuliu (num1,num2,product_name,product_address，product_time,logistics_name,logistics_address，logistics_time"
#                  "sale_name,sale_address，sale_time,information) "
#     "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [num1,num2,product_name,product_address,product_time,logistics_name,logistics_address,logistics_time,sale_name,sale_address,sale_time,information])
#   conn.commit()
#  return redirect('../')

# def add_product(request):
#  if request.method == 'GET':
#   return render(request, 'wuliu.html')
#  else:
#   product_name = request.POST.get('product_name', '')
#   product_address = request.POST.get('product_address', '')
#   product_time = request.POST.get('product_address', '')
#  conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="wuliu", charset='utf8')
#  with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
#   cursor.execute("INSERT INTO wuliu_wuliu (product_name,product_address,product_time) "
#     "values (%s,%s,%s)", [product_name,product_address,product_time])
#   conn.commit()
#  return redirect('../')
#
# def add_logistics(request):
#  if request.method == 'GET':
#   return render(request, 'wuliu.html')
#  else:
#   logistics_name = request.POST.get('logistics_name', '')
#   logistics_address = request.POST.get('logistics_address', '')
#   logistics_time = request.POST.get('logistics_address', '')
#  conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="wuliu", charset='utf8')
#  with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
#   cursor.execute("INSERT INTO wuliu_wuliu (logistics_name,logistics_address,logistics_time) "
#     "values (%s,%s,%s)", [logistics_name,logistics_address,logistics_time])
#   conn.commit()
#  return redirect('../')
#
# def add_sale(request):
#  if request.method == 'GET':
#   return render(request, 'wuliu.html')
#  else:
#   sale_name = request.POST.get('sale_name', '')
#   sale_address = request.POST.get('sale_address', '')
#   sale_time = request.POST.get('sale_address', '')
#  conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="wuliu", charset='utf8')
#  with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
#   cursor.execute("INSERT INTO wuliu_wuliu (sale_name,sale_address,sale_time) "
#     "values (%s,%s,%s)", [sale_name,sale_address,sale_time])
#   conn.commit()
#  return redirect('../')
# # 学生信息修改处理函数
# def edit(request):
#  if request.method == 'GET':
#   id = request.GET.get("id")
#  conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="sms", charset='utf8')
#  with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
#   cursor.execute("SELECT id,student_no,student_name FROM sims_student where id =%s", [id])
#   student = cursor.fetchone()
#  return render(request, 'student/edit.html', {'student': student})
#  else:
#    id = request.POST.get("id")
#  student_no = request.POST.get('student_no', '')
#  student_name = request.POST.get('student_name', '')
#  conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="sms", charset='utf8')
#  with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
#   cursor.execute("UPDATE sims_student set student_no=%s,student_name=%s where id =%s",
#     [student_no, student_name, id])
#   conn.commit()
#  return redirect('../')
#
# # 学生信息删除处理函数
# def delete(request):
#  id = request.GET.get("id")
#  conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="sms", charset='utf8')
#  with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
#  cursor.execute("DELETE FROM sims_student WHERE id =%s", [id])
#  conn.commit()
#  return redirect('../')