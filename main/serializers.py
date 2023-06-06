from rest_framework import serializers
from main.models import Employee, Leave

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'employee_name', 'contact_number', 'email', 'job_title', 'reporting_to', 'work_location')

class LeaveEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ('apply_date', 'nature_of_leave', 'first_day', 'last_day', 'number_of_days')

class LeaveAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ('__all__')