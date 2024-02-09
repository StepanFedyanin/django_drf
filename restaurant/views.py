from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from restaurant.models import Restaurant, Dish
from restaurant.serializers import RestaurantSerializer, DishSerializer, RestaurantCategoryDishSerializer
from restaurant.schemas import CreateRestaurantSchema, UpdateRestaurantSchema, DeleteSchema


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
        methods=['get'],
        url_path='(?P<id>[a-zA-Z0-9_]+)/category',
        url_name='by-category',
    )
    def get_category(self, request, id):
        restaurant = Restaurant.objects.get(id=id)
        serializer = RestaurantCategoryDishSerializer(restaurant.dishCategory.all(), many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    # @action(
    #     detail=False,
    #     methods=['post'],
    #     url_path='change',
    #     schema=UpdateRestaurantSchema(),
    # )
    # def change(self, request):
    #     restaurant = Restaurant.objects.get(id=request.data['id'])
    #     serializer = RestaurantSerializer(restaurant, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # @action(
    #     detail=False,
    #     methods=['post'],
    #     url_path='add',
    #     schema=CreateRestaurantSchema(),
    # )
    # def add(self, request):
    #     serializer = RestaurantSerializer(data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # @action(
    #     detail=False,
    #     methods=['post'],
    #     url_path='remove',
    #     url_name='remove',
    #     schema=DeleteSchema()
    # )
    # def remove(self, request):
    #     try:
    #         restaurant = Restaurant.objects.get(id=request.data['id'])
    #         restaurant.delete()
    #         return Response(status=status.HTTP_201_CREATED)
    #     except:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)

class DishViewSet(GenericViewSet):
    permission_classes = [AllowAny]

    def retrieve(self, request, pk=None):
        queryset = Dish.objects.all()
        restaurant = get_object_or_404(queryset, pk=pk)
        serializer = DishSerializer(restaurant)
        return Response(serializer.data)

    # @action(
    #     detail=False,
    #     methods=['post'],
    #     schema=CreateMenuSchema()
    # )
    # def add(self, request):
    #     serializer = MenuSerializer(data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderViewSet(GenericViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        queryset = Restaurant.objects.all()
        serializer = RestaurantSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(Restaurant, pk=pk)
        serializer = RestaurantSerializer(queryset)
        return Response(serializer.data)
