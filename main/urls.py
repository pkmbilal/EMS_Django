from django.urls import path
from main import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('employee_list/', views.EmployeeList, name='employee_list'),
    path('employee_add/', views.EmployeeAdd, name='employee_add'),
    path('employee_update/<int:id>/', views.EmployeeUpdate, name='employee_update'),
    path('employee_delete/<int:id>/', views.EmployeeDelete, name='employee_delete'),
]