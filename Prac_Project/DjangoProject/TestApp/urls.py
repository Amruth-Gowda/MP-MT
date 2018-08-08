from django.conf.urls import url
from . import views
from TestApp.views import EmployeeView 

urlpatterns = [
	url(r'^$', views.index, name='index' ),
	url(r'home.html$', views.index, name='index' ),
	url(r'emp_details.html$', views.emp_details, name='emp_details' ),
	url(r'add_employee.html$', EmployeeView.as_view(), name='add_employee'),
	url(r'about.html$', views.about, name='about' ),
	url(r'contact.html$', views.contact, name='contact' ),
]