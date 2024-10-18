from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Employee, Position


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    position = PositionSerializer()

    def update(self, instance, validated_data):
        position_data = validated_data.pop('position', None)
        if position_data:
            position_name = position_data.get('name')
            if position_name:
                position_instance, created = Position.objects.get_or_create(name=position_name)
                instance.position = position_instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = Employee
        fields = ['full_name', 'position', 'is_fired', 'date_of_termination']


class UserRegistrationSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=255)
    position_id = serializers.PrimaryKeyRelatedField(queryset=Position.objects.all(), source='position')
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'full_name', 'position_id']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        Employee.objects.create(
            user=user,
            full_name=validated_data['full_name'],
            position=validated_data['position']
        )
        return user
