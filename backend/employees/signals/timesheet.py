from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from ..models.timesheet import Timesheet

@receiver(pre_save, sender=Timesheet)
def validate_timesheet(sender, instance, **kwargs):
    """Validate timesheet data before saving"""
    instance.full_clean()

@receiver(post_save, sender=Timesheet)
def notify_timesheet_creation(sender, instance, created, **kwargs):
    """Handle notifications when a timesheet is created/updated"""
    if created:
        print(f"New timesheet created for {instance.employee}")
    else:
        print(f"Timesheet updated for {instance.employee}") 