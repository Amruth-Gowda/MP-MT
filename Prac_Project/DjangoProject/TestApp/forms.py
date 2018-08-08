from django import forms

class EmployeeForm(forms.Form):
	MID = forms.CharField(max_length=8)
	Name = forms.CharField(max_length=100)
	Email = forms.CharField(max_length=100)
	MobileNumber = forms.CharField(max_length=10)
	Address = forms.CharField(max_length=100)
	Designation = forms.CharField(max_length=100)
	
