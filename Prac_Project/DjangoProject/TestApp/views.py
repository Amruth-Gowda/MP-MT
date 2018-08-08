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
	id = []
	name = []
	email = [] 
	mobile = []
	address = []
	designation = []
	i = 0
	while count > 0:
		a, b, c, d, e, f = data[i]
		id.append(a)
		name.append(b)
		email.append(c)
		mobile.append(d)
		address.append(e)
		designation.append(f)
		i += 1
		count -= 1

	mylist = zip(id, name, email, mobile, address, designation)
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
			id = emp_data.cleaned_data['ID']
			name = emp_data.cleaned_data['Name']
			email = emp_data.cleaned_data['Email']
			mob_number = emp_data.cleaned_data['MobileNumber']
			address = emp_data.cleaned_data['Address']
			designation = emp_data.cleaned_data['Designation']
			print(id, name, email, mob_number, address, designation)
			query = "INSERT INTO mt_db.employee_details (id, emp_name, emp_email_id, emp_mobile_number, emp_address, emp_designation) VALUES (%s, %s, %s, %s, %s, %s)"
			print(query)
			connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='mt_db')
			e = connection.cursor()
			val = (id, name, email, mob_number, address, designation)
			count = e.execute(query, val)
			connection.commit()
			emp_data = EmployeeForm()
		
		return render(request, self.template_name, {'form': emp_data}) 		