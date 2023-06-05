from rest_framework import serializers
from main.models import Employee, Leave

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'employee_name', 'contact_number', 'email', 'job_title', 'reporting_to', 'work_location')