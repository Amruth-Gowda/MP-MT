from django.conf.urls import url
from . import views
from TestApp.views import EmployeeAdd
from TestApp.views import EmployeeDelete

urlpatterns = [
	url(r'^$', views.index, name='index' ),
	url(r'home.html$', views.index, name='index' ),
	url(r'emp_details.html$', views.emp_details, name='emp_details' ),
	url(r'add_employee.html$', EmployeeAdd.as_view(), name='add_employee'),
	url(r'delete_employee.html$', EmployeeDelete.as_view(), name='delete_employee'),
	url(r'about.html$', views.about, name='about' ),
	url(r'contact.html$', views.contact, name='contact' ),
]