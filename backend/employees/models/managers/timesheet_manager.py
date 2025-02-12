from django.db import models
from django.db.models import F, ExpressionWrapper, Sum, fields

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

    def get_total_hours(self, employee_id=None):
        """Calculate total hours worked"""
        queryset = self.all()
        if employee_id:
            queryset = queryset.filter(employee_id=employee_id)
        
        duration = ExpressionWrapper(
            F('end_time') - F('start_time'),
            output_field=fields.DurationField()
        )
        result = queryset.annotate(
            duration=duration
        ).aggregate(
            total_hours=Sum('duration')
        )
        
        total_seconds = result['total_hours'].total_seconds() if result['total_hours'] else 0
        return round(total_seconds / 3600, 2) 