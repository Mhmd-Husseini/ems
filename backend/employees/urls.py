from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeListView.as_view(), name='employee-list'),
    path('employees/create/', views.employee_create, name='employee-create'),
    path('employees/<int:pk>/', views.employee_detail, name='employee-detail'),
] 