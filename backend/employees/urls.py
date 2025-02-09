from django.urls import path
from . import views

urlpatterns = [
    path('employees/<int:pk>/', views.employee_detail, name='employee-detail'),
    path('employees/', views.employee_create, name='employee-create'),
] 