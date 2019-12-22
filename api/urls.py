from django.urls import path
from .views import DishView

urlpatterns = [
    path('dishes/', DishView.as_view(), name='dishes'),
]
