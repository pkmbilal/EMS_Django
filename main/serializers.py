from rest_framework import serializers
from main.models import Employee, Leave
from django.contrib.auth.models import User

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'employee_name', 'contact_number', 'email', 'job_title', 'reporting_to', 'work_location']

class EmployeeAddSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields ='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'