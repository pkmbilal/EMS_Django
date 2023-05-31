from django.contrib import admin
from main.models import Employee, Leave


class LeaveAdmin(admin.ModelAdmin):
    list_display = [all]
# Register your models here.
admin.site.register(Employee)
admin.site.register(Leave, LeaveAdmin)
