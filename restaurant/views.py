from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from restaurant.models import Restaurant

from restaurant.serializers import RestaurantSerializer


# Create your views here.
class RestaurantViewSet:
    def list(self, request):
        queryset = Restaurant.objects.all()
        serializer = RestaurantSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Restaurant.objects.filter(publication=True)
        user = get_object_or_404(queryset, pk=pk)
        serializer = RestaurantSerializer(user)
        return Response(serializer.data)
