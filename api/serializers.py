from rest_framework import serializers

from restaurant_menu.models import Dish


class DishSerializer(serializers.ModelSerializer):
    """Сериализатор блюд."""
    class Meta:
        model = Dish
        fields = '__all__'
