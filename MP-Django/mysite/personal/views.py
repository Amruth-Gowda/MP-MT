from django.views.generic import TemplateView

from personal.forms import EmployeeForm

from django.shortcuts import render

class EmployeeView(TemplateView):
	template_name = 'personal/home.html'

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
				
		