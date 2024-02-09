from rest_framework.serializers import ModelSerializer, SerializerMethodField

from restaurant.models import Restaurant, Dish, DishCategory


class DishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'description', 'price', 'image')

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['category'] = DishCategorySerializer(instance.category.all(), many=True).data
    #     return rep


class DishCategorySerializer(ModelSerializer):
    class Meta:
        model = DishCategory
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['dish'] = DishSerializer(instance.dish.all(), many=True).data
        return rep


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        print(instance.dishCategory.all())
        rep['categorys'] = DishCategorySerializer(instance.dishCategory.all(), many=True).data
        return rep


class RestaurantCategoryDishSerializer(ModelSerializer):
    class Meta:
        model = DishCategory
        fields = ('id', 'category', )
