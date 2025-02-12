from django.db import transaction
from django.core.exceptions import ValidationError
from ..models.employee import Employee
from ..models.timesheet import Timesheet

class EmployeeService:
    @staticmethod
    def create_employee(data):
        """Create a new employee with validation"""
        with transaction.atomic():
            employee = Employee(**data)
            employee.full_clean()
            employee.save()
            return employee

    @staticmethod
    def update_employee(employee_id, data):
        """Update employee information"""
        with transaction.atomic():
            employee = Employee.objects.get(id=employee_id)
            for key, value in data.items():
                setattr(employee, key, value)
            employee.full_clean()
            employee.save()
            return employee

    @staticmethod
    def delete_employee(employee_id):
        """Delete employee and related data"""
        with transaction.atomic():
            employee = Employee.objects.get(id=employee_id)
            employee.delete()

    @staticmethod
    def get_employee_stats(employee_id):
        """Get employee statistics"""
        employee = Employee.objects.get(id=employee_id)
        timesheets = Timesheet.objects.for_employee(employee_id)
        
        total_hours = timesheets.get_total_hours()
        timesheet_count = timesheets.count()
        
        return {
            'employee': employee,
            'total_hours': total_hours,
            'timesheet_count': timesheet_count,
            'average_hours_per_timesheet': round(total_hours / timesheet_count, 2) if timesheet_count > 0 else 0
        }

    @staticmethod
    def get_department_stats():
        """Get statistics by department"""
        from django.db.models import Count, Avg
        return Employee.objects.values('department').annotate(
            employee_count=Count('id'),
            avg_salary=Avg('salary')
        ) 