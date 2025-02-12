from rest_framework import serializers
from ...models.employee import Employee

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