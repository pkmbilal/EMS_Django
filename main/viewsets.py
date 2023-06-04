from rest_framework import viewsets, permissions, request
from main.serializers import EmployeeSerializer, EmployeeAddSerializer, UserSerializer
from main.models import Employee
from django.contrib.auth.models import User

class EmployeeListViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ['get']
    permission_classes = [permissions.IsAdminUser]

class EmployeeAddViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeAddSerializer
    http_method_names = ['post']
    permission_classes = [permissions.IsAdminUser]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    
