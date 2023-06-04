from django.urls import path,include
from rest_framework import routers
from main.viewsets import EmployeeListViewSet, EmployeeAddViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'employee_list', EmployeeListViewSet)
router.register(r'employee_add', EmployeeAddViewSet)
router.register(r'user_list', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]