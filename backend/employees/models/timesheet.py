from django.db import models
from django.core.exceptions import ValidationError
from .base import TimeStampedModel
from .managers.timesheet_manager import TimesheetManager
from .employee import Employee

class Timesheet(TimeStampedModel):
    """Timesheet model for tracking employee work hours"""
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='timesheets',
        help_text="Employee this timesheet belongs to"
    )
    start_time = models.DateTimeField(
        help_text="Start time of work period"
    )
    end_time = models.DateTimeField(
        help_text="End time of work period"
    )
    summary = models.TextField(
        blank=True,
        help_text="Summary of work done"
    )

    objects = TimesheetManager()

    class Meta:
        ordering = ['-start_time']
        verbose_name = 'Timesheet'
        verbose_name_plural = 'Timesheets'
        indexes = [
            models.Index(fields=['-start_time']),
            models.Index(fields=['employee']),
        ]

    def clean(self):
        super().clean()
        if self.start_time and self.end_time:
            if self.start_time >= self.end_time:
                raise ValidationError({
                    'end_time': 'End time must be after start time.'
                })

    def __str__(self):
        return f"{self.employee} - {self.start_time.date()}"

    def get_duration(self):
        """Calculate duration in hours"""
        if self.start_time and self.end_time:
            duration = self.end_time - self.start_time
            return round(duration.total_seconds() / 3600, 2) 