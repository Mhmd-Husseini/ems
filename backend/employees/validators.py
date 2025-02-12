from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_future_date(value):
    """Validate that a date is not in the future"""
    if value > timezone.now().date():
        raise ValidationError('Date cannot be in the future.') 