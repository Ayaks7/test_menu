from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from api.serializers import DishSerializer
from api.auth import SingleTokenAuthentication
from restaurant_menu.models import Dish


class DishView(APIView):
    """Апи для получения и добавления блюд."""
    authentication_classes = (SingleTokenAuthentication,)

    def get(self, request):
        dishes = Dish.objects.all()
        serializer = DishSerializer(dishes, many=True)
        return Response({"dishes": serializer.data})

    def post(self, request):
        dish = dict(request.data)
        dish = {k: v[0] for k, v in dish.items()}

        serializer = DishSerializer(data=dish)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
