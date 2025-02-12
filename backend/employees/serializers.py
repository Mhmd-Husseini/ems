from rest_framework import serializers
from .models import Employee, Timesheet

class EmployeeListSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Employee
        fields = ['id', 'full_name', 'job_title', 'department', 'email']
        
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

class EmployeeSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False, allow_null=True)
    cv = serializers.FileField(required=False, allow_null=True)
    id_document = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = Employee
        fields = '__all__'

    def validate(self, data):
        for field in ['photo', 'cv', 'id_document']:
            if field in data and data[field] is None:
                data.pop(field)
        return data

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