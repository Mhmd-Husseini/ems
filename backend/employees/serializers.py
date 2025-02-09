from rest_framework import serializers
from .models import Employee

class EmployeeListSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Employee
        fields = ['id', 'full_name', 'job_title', 'department', 'email']
        
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

class EmployeeSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)
    cv = serializers.FileField(required=False)
    id_document = serializers.FileField(required=False)

    class Meta:
        model = Employee
        fields = '__all__' 