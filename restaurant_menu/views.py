from django.shortcuts import render
from django.db.models import Sum
from django.http import Http404
from django.views.generic.list import ListView

from restaurant_menu.models import (
    DishCategory,
    Dish
)


class DishCategoryListView(ListView):
    model = DishCategory
    template_name = 'menu.html'


def order_view(request):
    context = {}
    if request.method == 'GET':
        raise Http404()

    dishes_ids = request.POST.getlist('dishes', [])
    if dishes_ids:
        dishes = Dish.objects.filter(id__in=dishes_ids)

        full_price = dishes.aggregate(
            full_price=Sum('price')
        ).get('full_price')

        context['dishes'] = dishes
        context['full_price'] = full_price
    return render(request, 'order.html', context)
