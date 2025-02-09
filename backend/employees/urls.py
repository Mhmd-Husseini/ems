from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeListView.as_view(), name='employee-list'),
    path('employees/create/', views.employee_create, name='employee-create'),
    path('employees/<int:pk>/', views.employee_detail, name='employee-detail'),
    path('timesheets/', views.TimesheetListView.as_view(), name='timesheet-list'),
    path('timesheets/<int:pk>/', views.TimesheetDetailView.as_view(), name='timesheet-detail'),
    path('employee-options/', views.employee_options, name='employee-options'),
] 