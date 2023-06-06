from django.urls import path
from main import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('employee_list/', views.EmployeeList, name='employee_list'),
    path('employee_add/', views.EmployeeAdd, name='employee_add'),
    path('employee_details/<int:id>/', views.EmployeeDetails, name='employe_details'),
    path('employee_update/<int:id>/', views.EmployeeUpdate, name='employee_update'),
    path('employee_delete/<int:id>/', views.EmployeeDelete, name='employee_delete'),
    path('leave_list', views.LeaveList, name='leave_list'),

    path('leave_add', views.LeaveApply, name='leave_add'),
]