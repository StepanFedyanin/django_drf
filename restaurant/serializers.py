from rest_framework.serializers import ModelSerializer, SerializerMethodField

from restaurant.models import Restaurant, Menu, Dish


class DishSerializer(ModelSerializer):
    # photo_url = SerializerMethodField()

    class Meta:
        model = Dish
        fields = '__all__'


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'type')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['dish'] = DishSerializer(instance.dish.all(), many=True).data
        return rep

    # def get_photo_url(self, image):
    #     request = self.context.get('request')
    #     photo_url = Dish.image.url
    #     return request.build_absolute_uri(photo_url)


class MenuRestaurantSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'type')


class RestaurantSerializer(ModelSerializer):

    def validate(self, attrs):
        # print(attrs)
        # menus = attrs.pop('menus', None)
        
        # if not attrs.instance and menus:
        #     menu = Menu.objects.get(id=menus.id)
        #     print(menu)
        #     # validated_data.update(menus=menu)
        return super().validate(attrs)

    class Meta:
        model = Restaurant
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['menus'] = MenuRestaurantSerializer(instance.menus.all(), many=True).data
        return rep
