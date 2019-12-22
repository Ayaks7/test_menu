from django.contrib import admin
from .models import (
    DishCategory,
    Dish,
    Allergen
)

admin.site.register(DishCategory)
admin.site.register(Dish)
admin.site.register(Allergen)
