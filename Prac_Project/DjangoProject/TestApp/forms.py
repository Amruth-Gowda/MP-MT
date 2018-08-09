from django import forms

class EmployeeForm(forms.Form):
	ID = forms.IntegerField()
	Name = forms.CharField(max_length=100)
	Email = forms.EmailField()
	MobileNumber = forms.CharField(max_length=10)
	Address = forms.CharField(max_length=100)
	Designation = forms.CharField(max_length=100)
	

class EmployeeDeleteForm(forms.Form):
	ID = forms.IntegerField()
	
