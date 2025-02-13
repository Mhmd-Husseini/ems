from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.core.management import call_command

def seed_data(sender, **kwargs):
    """Only seed after all migrations are done"""
    try:
        call_command('seed_data')
    except Exception as e:
        print(f"Error seeding database: {str(e)}")

class EmployeesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'employees'
    verbose_name = 'Employee Management'

    def ready(self):
        try:
            from .signals import employee, timesheet
            from .utils.filters import EmployeeFilter
            from .models import Employee
            from . import enums  # Ensure enums are loaded
            
            EmployeeFilter._meta.model = Employee
            post_migrate.connect(seed_data, sender=self)
        except Exception as e:
            print(f"Error in app ready: {str(e)}")
