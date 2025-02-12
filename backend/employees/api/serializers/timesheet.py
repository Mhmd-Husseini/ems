from rest_framework import serializers
from ...models.timesheet import Timesheet
from ...models.employee import Employee

class TimesheetSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        required=True
    )

    class Meta:
        model = Timesheet
        fields = ['id', 'employee', 'start_time', 'end_time', 'summary']
        
    def validate(self, data):
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError({
                'end_time': 'End time must be after start time.'
            })
        return data

class TimesheetListSerializer(serializers.ModelSerializer):
    employee_name = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()
    
    class Meta:
        model = Timesheet
        fields = ['id', 'employee_name', 'start_time', 'end_time', 'duration', 'summary']
        
    def get_employee_name(self, obj):
        return f"{obj.employee.first_name} {obj.employee.last_name}"
        
    def get_duration(self, obj):
        duration = obj.end_time - obj.start_time
        hours = duration.total_seconds() / 3600
        return round(hours, 2) 