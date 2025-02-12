from django.db import transaction
from django.core.exceptions import ValidationError
from ..models.timesheet import Timesheet

class TimesheetService:
    @staticmethod
    def create_timesheet(data):
        """Create a new timesheet with validation"""
        with transaction.atomic():
            timesheet = Timesheet(**data)
            timesheet.full_clean()
            timesheet.save()
            return timesheet

    @staticmethod
    def get_employee_timesheets(employee_id, start_date=None, end_date=None):
        """Get employee timesheets with optional date range"""
        timesheets = Timesheet.objects.for_employee(employee_id)
        if start_date and end_date:
            timesheets = timesheets.in_date_range(start_date, end_date)
        return timesheets

    @staticmethod
    def get_timesheet_summary(employee_id, start_date=None, end_date=None):
        """Get summary of employee's work hours"""
        timesheets = TimesheetService.get_employee_timesheets(
            employee_id, start_date, end_date
        )
        total_hours = timesheets.get_total_hours()
        timesheet_count = timesheets.count()
        
        return {
            'total_hours': total_hours,
            'timesheet_count': timesheet_count,
            'average_hours': round(total_hours / timesheet_count, 2) if timesheet_count > 0 else 0
        } 