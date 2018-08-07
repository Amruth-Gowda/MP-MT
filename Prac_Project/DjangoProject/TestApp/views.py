from django.shortcuts import render
import pymysql
connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='mt_db')
e = connection.cursor()
query = 'select * from `employee_details`;'
count = e.execute(query)
data = e.fetchall()
mid = []
name = []
email = [] 
mobile = []
address = []
designation = []
i = 0
while count > 0:
	a, b, c, d, e, f = data[i]
	mid.append(a)
	name.append(b)
	email.append(c)
	mobile.append(d)
	address.append(e)
	designation.append(f)
	i += 1
	count -= 1

mylist = zip(mid, name, email, mobile, address, designation)

def index(request):
	return render(request, 'TestApp/home.html')
	
def emp_details(request):
	return render(request, 'TestApp/emp_details.html', {'mylist' : mylist})
	
def about(request):
	return render(request, 'TestApp/about.html')

def contact(request):
	return render(request, 'TestApp/contact.html')