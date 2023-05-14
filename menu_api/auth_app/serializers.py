from rest_framework import serializers

from auth_app.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        user = Employee.objects.create_user(**validated_data)
        user.is_active = True
        user.save()
        return user
    