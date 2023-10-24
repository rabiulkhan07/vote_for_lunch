from rest_framework import serializers
from .models import Restaurant,Menu

class RestaurantSerializer(serializers.ModelSerializer):
    created_by_name = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'created_by_name')

    def get_created_by_name(self, obj):
        return obj.creator_name()
class MenuSerializer(serializers.ModelSerializer):
    created_by_name = serializers.SerializerMethodField()
    restaurent_name = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = '__all__'

    def get_created_by_name(self, obj):
        return obj.creator_name()
    def get_restaurent_name(self, obj):
        return obj.restaurent_name()
