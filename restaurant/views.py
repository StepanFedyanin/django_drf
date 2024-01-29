
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action

from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from restaurant.models import Restaurant, Menu

from restaurant.serializers import RestaurantSerializer, MenuSerializer


# Create your views here.
class RestaurantViewSet(GenericViewSet):
    permission_classes = [AllowAny]

    # def list(self, request):
    #     queryset = Restaurant.objects.filter(published = True)
    #     serializer = RestaurantSerializer(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Restaurant.objects.all()
        restaurant = get_object_or_404(queryset, pk=pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)


class MenuViewSet(GenericViewSet):
    permission_classes = [AllowAny]

    @action(
        detail=False,
        methods=['get'],
        url_path='by_id/(?P<by_id>[a-zA-Z0-9_]+)',
        url_name='by_id',
    )
    def menu_by_restaurant(self, request, by_id):
        queryset = Menu.objects.filter(id__in=by_id)
        print(queryset)
        # serializer = MenuSerializer(queryset, many=True)
        return Response({}, status=status.HTTP_200_OK)

