from django.contrib import admin
from main.models import Employee, Leave


class LeaveAdmin(admin.ModelAdmin):
    list_display = [all]

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee_name', 'contact_number', 'email', 'position', 'reporting_to', 'work_location']

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Leave, LeaveAdmin)
