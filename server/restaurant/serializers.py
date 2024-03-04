from rest_framework.serializers import ModelSerializer

from server.restaurant.models import Restaurant, Dish, DishCategory, Order, OrderItem


class DishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'description', 'price', 'image')


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
        rep['categorys'] = DishCategorySerializer(instance.dishCategory.all(), many=True).data
        return rep


class RestaurantCategoryDishSerializer(ModelSerializer):
    class Meta:
        model = DishCategory
        fields = ('id', 'category',)


class OrderItemPostSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'quantity')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep = DishSerializer(instance.dish).data
        rep['quantity'] = 0
        if not (instance.id is None):
            rep['order_item'] = instance.id
            rep['quantity'] = instance.quantity
        return rep


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'total_price')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['order_dish'] = OrderItemSerializer(instance.order_dish.all(), many=True).data
        return rep
