from django.db import models
from django.db.models import Q

class EmployeeManager(models.Manager):
    def active(self):
        """Return only active employees"""
        return self.filter(is_active=True)

    def search(self, query):
        """Search employees by name, email, or department"""
        return self.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query) |
            Q(department__icontains=query)
        )

    def by_department(self, department):
        """Get employees by department"""
        return self.filter(department=department)

class TimesheetManager(models.Manager):
    def for_employee(self, employee_id):
        """Get timesheets for a specific employee"""
        return self.filter(employee_id=employee_id)

    def in_date_range(self, start_date, end_date):
        """Get timesheets within a date range"""
        return self.filter(
            start_time__date__gte=start_date,
            end_time__date__lte=end_date
        ) 