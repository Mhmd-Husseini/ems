from django.db import models
from django.core.validators import MinValueValidator, EmailValidator
from django.core.exceptions import ValidationError
from decimal import Decimal
from .managers import EmployeeManager, TimesheetManager
from .validators import validate_future_date

class TimeStampedModel(models.Model):
    """Abstract base class with created and updated timestamps"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Employee(TimeStampedModel):
    """Employee model for storing employee information"""
    # Personal Information
    first_name = models.CharField(
        max_length=50,
        help_text="Employee's first name"
    )
    last_name = models.CharField(
        max_length=50,
        help_text="Employee's last name"
    )
    email = models.EmailField(
        unique=True,
        validators=[EmailValidator()],
        help_text="Employee's email address"
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        help_text="Employee's phone number"
    )
    date_of_birth = models.DateField(
        help_text="Employee's date of birth"
    )
    
    # Employment Information
    job_title = models.CharField(
        max_length=100,
        help_text="Employee's job title"
    )
    department = models.CharField(
        max_length=100,
        help_text="Employee's department"
    )
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('15000.00'))],
        help_text="Employee's annual salary"
    )
    start_date = models.DateField(
        validators=[validate_future_date],
        help_text="Employee's start date"
    )
    
    # Documents - all optional
    photo = models.ImageField(
        upload_to='uploads/photos/',
        blank=True,
        null=True,
        help_text="Employee's photo (optional)"
    )
    cv = models.FileField(
        upload_to='uploads/documents/cv/',
        blank=True,
        null=True,
        help_text="Employee's CV (optional)"
    )
    id_document = models.FileField(
        upload_to='uploads/documents/id/',
        blank=True,
        null=True,
        help_text="Employee's ID document (optional)"
    )

    objects = EmployeeManager()

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['email']),
            models.Index(fields=['department']),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        super().clean()
        if self.date_of_birth and self.start_date:
            if self.date_of_birth > self.start_date:
                raise ValidationError({
                    'start_date': 'Start date cannot be before date of birth.'
                })

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