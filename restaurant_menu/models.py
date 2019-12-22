from django.db import models

from restaurant_menu.utils import dich_image_path


class DishCategory(models.Model):
    """Категория блюда."""
    name = models.CharField('Наменование', max_length=64)

    def __str__(self, *args, **kwargs):
        return self.name


class Dish(models.Model):
    """Блюда."""
    name = models.CharField('Наменование', max_length=64, unique=True)
    price = models.PositiveIntegerField('Цена')
    calorie_content = models.FloatField('Калорийность')

    image = models.ImageField(
        'Изображение',
        upload_to=dich_image_path,
        max_length=256,
        blank=True
    )
    category = models.ForeignKey(
        DishCategory,
        verbose_name='Категория',
        related_name='dishes',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self, *args, **kwargs):
        return self.name


class Allergen(models.Model):
    """Аллергены."""
    name = models.CharField('Наменование', max_length=64)
    dish = models.ManyToManyField(
        Dish,
        verbose_name='Аллерген',
        related_name='allergens',
    )

    def __str__(self, *args, **kwargs):
        return self.name
