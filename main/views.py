from django.shortcuts import redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from main.models import Employee, Leave
from main.serializers import EmployeeSerializer, LeaveEmployeeSerializer, LeaveAdminSerializer
from rest_framework import status



# For ADMIN Only!!!!
#---------------------

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Employee List' : '/employee_list',
        'Add Employee' : '/employee_add',
        'Employee Details' : '/employee_details/id',   
        'Update Employee' : '/employee_update/id',
        'Delete Employee' : '/employee_delete/id',
    }

    return Response(api_urls)

# Displays Total Employee List
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def EmployeeList(request):
    employee = Employee.objects.all()
    serializer = EmployeeSerializer(employee, many=True)
    return Response(serializer.data)

# Create an Employee
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def EmployeeAdd(request):
    employee = EmployeeSerializer(data=request.data)
    if employee.is_valid():
        employee.save()
        return Response(employee.data)
    else:
        return Response('Enter correct informations !!!')

# Displays Individual Employee Details    
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def EmployeeDetails(request, id):
    employee = Employee.objects.get(id=id)
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)

# Update a Single Employee    
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def EmployeeUpdate(request, id):
    employee = Employee.objects.get(id=id)
    serializer = EmployeeSerializer(instance=employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# Delete an Employee
@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def EmployeeDelete(request, id):
    employee=Employee.objects.filter(id=id)
    if id == id:
        employee.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
# List of Employee Leaves
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def LeaveList(request):
    leave = Leave.objects.all()
    serializer = LeaveAdminSerializer(leave, many=True)
    return Response(serializer.data)
    

# For EMPLOYEE Only!!!!
#---------------------

@api_view(['GET','POST'])
def LeaveApply(request):
    serializer = LeaveAdminSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)