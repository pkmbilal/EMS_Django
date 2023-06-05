from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Employee, Leave
from main.serializers import EmployeeSerializer
from rest_framework import status


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Employee List' : '/employee_list',
        'Add Employee' : '/employee_add',
        'Update Employee' : '/employee_update/id',
        'Delete Employee' : '/employee_delete/id',
    }

    return Response(api_urls)

@api_view(['GET'])
def EmployeeList(request):
    employee = Employee.objects.all()
    serializer = EmployeeSerializer(employee, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def EmployeeAdd(request):
    employee = EmployeeSerializer(data=request.data)
    if employee.is_valid():
        employee.save()
        return Response(employee.data)
    else:
        return Response('Enter correct informations !!!')
    
@api_view(['POST'])
def EmployeeUpdate(request, id):
    employee = Employee.objects.get(id=id)
    serializer = EmployeeSerializer(instance=employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['DELETE'])
def EmployeeDelete(request, id):
    employee=Employee.objects.filter(id=id)
    if id == id:
        employee.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    