from django.conf.urls import url
from personal.views import EmployeeView 

urlpatterns = [
		url(r'^$', EmployeeView.as_view(), name='employee')
]