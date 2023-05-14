from rest_framework import serializers

from core_app.models import Restaurant, Menu


class MenuSerializer(serializers.ModelSerializer):
    votes_count = serializers.IntegerField(source='get_votes_count', required=False)
    restaurant_id = serializers.IntegerField(source='restaurant.pk', required=False)

    class Meta:
        model = Menu
        fields = ['pk', 'items', 'date', 'restaurant_id', 'votes_count']


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = '__all__'
