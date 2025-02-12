from django.contrib import admin
from .models import Employee, Timesheet

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'job_title')
    list_filter = ('department', 'job_title')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('last_name', 'first_name')

@admin.register(Timesheet)
class TimesheetAdmin(admin.ModelAdmin):
    list_display = ('employee', 'start_time', 'end_time', 'get_duration')
    list_filter = ('employee', 'start_time')
    search_fields = ('employee__first_name', 'employee__last_name', 'summary')
    ordering = ('-start_time',)
