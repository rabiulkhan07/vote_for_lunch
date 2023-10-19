from rest_framework import serializers
from .models import Employee
from django.contrib.auth.hashers import make_password

class EmployeeSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Employee
        fields = ['id','fullname','email','employeeId','password','presentAddress','contactNo']

        extra_kwargs = {
            'password' : {'write_only':True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)

        if password is not None :
            instance.set_password(password)
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password',None)
        if password is not None :
            instance.set_password(password)
        return super().update(instance, validated_data)