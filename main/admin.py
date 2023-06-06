from django.contrib import admin
from main.models import Employee, Leave


class LeaveAdmin(admin.ModelAdmin):
    list_display = ['employee_name', 'apply_date', 'nature_of_leave', 'first_day', 'last_day', 'number_of_days']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee_name', 'contact_number', 'email', 'position', 'reporting_to', 'work_location']

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Leave, LeaveAdmin)
