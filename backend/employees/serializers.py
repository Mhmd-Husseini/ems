from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)
    cv = serializers.FileField(required=False)
    id_document = serializers.FileField(required=False)

    class Meta:
        model = Employee
        fields = '__all__' 