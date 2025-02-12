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

    def with_documents(self):
        """Get employees who have uploaded documents"""
        return self.filter(
            Q(photo__isnull=False) |
            Q(cv__isnull=False) |
            Q(id_document__isnull=False)
        ) 