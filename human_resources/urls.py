from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='humanResources_Main'),
    url(r'^all_employees/$', views.employees, name='all_employees'),
    url(r'^all_leave/$', views.leave, name='all_leave'),
    url(r'^all_roles/$', views.roles, name='all_roles'),
    url(r'^employee_new/$', views.employee_new, name='employee_new'),
    url(r'^role_new/$', views.role_new, name='role_new'),
]
