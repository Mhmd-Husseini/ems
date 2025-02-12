from django.apps import AppConfig


class EmployeesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'employees'
    verbose_name = 'Employee Management'

    def ready(self):
        from .signals import employee, timesheet
        from .utils.filters import EmployeeFilter
        from .models import Employee
        
        EmployeeFilter._meta.model = Employee
