from django.views.generic import TemplateView

from TestApp.forms import EmployeeForm

from django.shortcuts import render

import pymysql

def index(request):
	return render(request, 'TestApp/home.html')
	
def emp_details(request):
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
	return render(request, 'TestApp/emp_details.html', {'mylist' : mylist})
	
def about(request):
	return render(request, 'TestApp/about.html')

def contact(request):
	return render(request, 'TestApp/contact.html')
	

class EmployeeView(TemplateView):
	template_name = 'TestApp/add_employee.html'

	def get(self, request):
		emp_data = EmployeeForm()
		return render(request, self.template_name, {'form': emp_data}) 
		
	def post(self, request):
		emp_data = EmployeeForm(request.POST)
		if emp_data.is_valid():
			mid = emp_data.cleaned_data['MID']
			name = emp_data.cleaned_data['Name']
			email = emp_data.cleaned_data['Email']
			mob_number = emp_data.cleaned_data['MobileNumber']
			address = emp_data.cleaned_data['Address']
			designation = emp_data.cleaned_data['Designation']
			print(mid, name, email, mob_number, address, designation)
			emp_data = EmployeeForm()
		return render(request, self.template_name, {'form': emp_data}) 		