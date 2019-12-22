from django.urls import path
from .views import (
    DishCategoryListView,
    order_view
)


urlpatterns = [
    path('', DishCategoryListView.as_view(), name='main_list'),
    path('order/', order_view, name='order'),
]
