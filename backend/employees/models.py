from django.db import models
from django.core.validators import MinValueValidator, EmailValidator
from datetime import date
from decimal import Decimal
from django.core.exceptions import ValidationError

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    phone = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField()
    
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('15000.00'))]
    )
    start_date = models.DateField()
    
    photo = models.ImageField(
        upload_to='uploads/photos/',
        blank=True,
        null=True
    )
    cv = models.FileField(
        upload_to='uploads/documents/cv/',
        blank=True,
        null=True
    )
    id_document = models.FileField(
        upload_to='uploads/documents/id/',
        blank=True,
        null=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Timesheet(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='timesheets'
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_time']

    def clean(self):
        if self.start_time and self.end_time and self.start_time >= self.end_time:
            raise ValidationError({
                'end_time': 'End time must be after start time.'
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee} - {self.start_time.date()}" 