import coreapi
import coreschema
from rest_framework.schemas import AutoSchema


class MenuSchema(AutoSchema):
    def get_serializer_fields(self, path, method):
        return [
            coreapi.Field(
                name='type',
                location='form',
                required=True,
                schema=coreschema.String(description='Тип меню')
            ),
            coreapi.Field(
                name='dish',
                location='form',
                required=True,
                schema=coreschema.Array(description='Список блюд')
            )
        ]

class RestaurantSchema(AutoSchema):
    def get_serializer_fields(self, path, method):
        return [
            coreapi.Field(
                name='name',
                location='form',
                required=True,
                schema=coreschema.String(description='Название ресторана')
            ),
            coreapi.Field(
                name='address',
                location='form',
                required=True,
                schema=coreschema.String(description='Адрес')
            ),
            coreapi.Field(
                name='dish',
                location='form',
                required=True,
                schema=coreschema.Array(description='Меню')
            )
        ]