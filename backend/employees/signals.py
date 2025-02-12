from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Employee, Timesheet
import os

@receiver(pre_save, sender=Employee)
def validate_employee(sender, instance, **kwargs):
    """Validate employee data before saving"""
    instance.full_clean()

@receiver(pre_delete, sender=Employee)
def cleanup_employee_files(sender, instance, **kwargs):
    """Clean up employee files when employee is deleted"""
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)
    
    if instance.cv:
        if os.path.isfile(instance.cv.path):
            os.remove(instance.cv.path)
    
    if instance.id_document:
        if os.path.isfile(instance.id_document.path):
            os.remove(instance.id_document.path)

@receiver(pre_save, sender=Timesheet)
def validate_timesheet(sender, instance, **kwargs):
    """Validate timesheet data before saving"""
    instance.full_clean()

@receiver(post_save, sender=Timesheet)
def notify_timesheet_creation(sender, instance, created, **kwargs):
    """
    Signal to handle notifications when a timesheet is created/updated
    You can extend this to send emails, notifications, etc.
    """
    if created:
        print(f"New timesheet created for {instance.employee}")
    else:
        print(f"Timesheet updated for {instance.employee}") 