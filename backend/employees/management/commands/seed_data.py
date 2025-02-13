from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from datetime import timedelta
import random
from employees.models import Employee, Timesheet
from employees.enums import Department, JobPosition

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting database seeding...')
        
        try:
            with transaction.atomic():
                if not Employee.objects.exists():
                    self._create_employees()
                    self._create_timesheets()
                    self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))
                else:
                    self.stdout.write(self.style.WARNING('Database already contains data. Skipping seeding.'))
        
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error seeding database: {str(e)}'))

    def _create_employees(self):
        employees_data = [
            {
                'first_name': 'John',
                'last_name': 'Doe',
                'email': 'john.doe@example.com',
                'phone': '123-456-7890',
                'department': Department.ENGINEERING.value,
                'job_title': JobPosition.SENIOR_DEVELOPER.value,
                'salary': 85000,
                'date_of_birth': '1990-01-15',
                'start_date': '2022-01-01',
            },
            {
                'first_name': 'Jane',
                'last_name': 'Smith',
                'email': 'jane.smith@example.com',
                'phone': '123-456-7891',
                'department': Department.MARKETING.value,
                'job_title': JobPosition.MARKETING_MANAGER.value,
                'salary': 75000,
                'date_of_birth': '1992-05-20',
                'start_date': '2022-02-01',
            },
            # Add more sample employees as needed
        ]

        for data in employees_data:
            Employee.objects.create(**data)
            self.stdout.write(f'Created employee: {data["first_name"]} {data["last_name"]}')

    def _create_timesheets(self):
        employees = Employee.objects.all()
        now = timezone.now()
        
        for employee in employees:
            # Create timesheets for the last 30 days
            for day in range(30):
                start_date = now - timedelta(days=day)
                start_time = start_date.replace(hour=2, minute=0)
                end_time = start_date.replace(hour=11, minute=0)
                
                Timesheet.objects.create(
                    employee=employee,
                    start_time=start_time,
                    end_time=end_time,
                    summary=f'Regular work day for {employee.first_name}'
                ) 