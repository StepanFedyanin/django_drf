from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from restaurant.models import Restaurant, Menu, Dish
from restaurant.serializers import RestaurantSerializer, MenuSerializer, DishSerializer
from restaurant.schemas import MenuSchema, RestaurantSchema


# Create your views here.
class RestaurantViewSet(GenericViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        queryset = Restaurant.objects.all()
        serializer = RestaurantSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(Restaurant, pk=pk)
        serializer = RestaurantSerializer(queryset)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=['post'],
        schema=RestaurantSchema(),
    )
    def add(self, request):
        print(request.data)
        serializer = RestaurantSerializer(data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuViewSet(GenericViewSet):
    permission_classes = [AllowAny]

    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(Menu, pk=pk)
        serializer = MenuSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=['post'],
        schema=MenuSchema()
    )
    def add(self, request):
        # queryset = Menu.objects.filter(id__in=by_id)
        # print(queryset)
        # # serializer = MenuSerializer(queryset, many=True)
        return Response({}, status=status.HTTP_200_OK)


class DishViewSet(GenericViewSet):
    permission_classes = [AllowAny]

    def retrieve(self, request, pk=None):
        queryset = Dish.objects.all()
        restaurant = get_object_or_404(queryset, pk=pk)
        serializer = DishSerializer(restaurant)
        return Response(serializer.data)
