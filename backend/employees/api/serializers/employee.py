from rest_framework import serializers
from ...models.employee import Employee
from ...enums import Department, JobPosition

class EmployeeListSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Employee
        fields = ['id', 'full_name', 'job_title', 'department', 'email', 'salary', 'start_date', 'phone', 'date_of_birth']
        
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

class EmployeeSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False, allow_null=True)
    cv = serializers.FileField(required=False, allow_null=True)
    id_document = serializers.FileField(required=False, allow_null=True)
    department_display = serializers.CharField(source='get_department_display', read_only=True)
    job_title_display = serializers.CharField(source='get_job_title_display', read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'

    def validate(self, data):
        for field in ['photo', 'cv', 'id_document']:
            if field in data and data[field] is None:
                data.pop(field)
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['department_choices'] = Department.choices
        data['job_title_choices'] = JobPosition.choices
        return data 