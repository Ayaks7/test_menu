import os
import io
from PIL import Image
from django.conf import settings
from rest_framework import status
from rest_framework.test import APITestCase

from restaurant_menu.models import Dish


class DishAddTests(APITestCase):
    """Тестируем создание блюда через API."""
    def setUp(self):
        self.url = 'http://0.0.0.0:8000/api/dishes/'

    def tearDown(self):
        dish = Dish.objects.first()
        if dish:
            os.remove(dish.image.path)

    @staticmethod
    def create_data():
        """Генерируем данные для объекта."""
        return {
            'name': 'test_dish',
            'price': 100,
            'calorie_content': 35,
            'image': DishAddTests.create_image()
        }

    @staticmethod
    def create_image():
        """Генерируем изображение."""
        f = io.BytesIO()
        img = Image.new('RGB', (60, 30), color='red')
        img.save(f, 'png')
        f.name = 'test_image.png'
        f.seek(0)
        return f

    def test_create_dish(self):
        """Тест создания объекта."""
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + settings.API_TOKEN
        )
        response = self.client.post(
            self.url, data=self.create_data(), format='multipart'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dish.objects.count(), 1)

        dish = Dish.objects.first()
        image_path = f'{settings.MEDIA_ROOT}/dish_images/test_dish_image.png'
        self.assertEqual(dish.name, 'test_dish')
        self.assertEqual(dish.price, 100)
        self.assertEqual(dish.calorie_content, 35)
        self.assertEqual(dish.image.path,  image_path)

    def test_incorrect_token(self):
        """Тест невалидного значения токена."""
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + settings.API_TOKEN + '1'
        )
        response = self.client.post(
            self.url, self.create_data(), format='multipart'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_missing_token(self):
        """Тест запроса без токена."""
        response = self.client.post(
            self.url, self.create_data(), format='multipart'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
