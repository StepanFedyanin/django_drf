import coreapi
import coreschema
from rest_framework.schemas import AutoSchema


# class CreateMenuSchema(AutoSchema):
#     def get_serializer_fields(self, path, method):
#         return [
#             coreapi.Field(
#                 name='type',
#                 location='form',
#                 required=True,
#                 schema=coreschema.String(description='Тип меню')
#             ),
#             coreapi.Field(
#                 name='dish',
#                 location='form',
#                 required=True,
#                 schema=coreschema.Array(description='Список блюд')
#             )
#         ]


# class UpdateMenuSchema(AutoSchema):
#     def get_serializer_fields(self, path, method):
#         return [
#             coreapi.Field(
#                 name='id',
#                 location='form',
#                 required=True,
#                 schema=coreschema.String(description='id меняемого меню')
#             ),
#             coreapi.Field(
#                 name='type',
#                 location='form',
#                 required=True,
#                 schema=coreschema.String(description='Тип меню')
#             ),
#             coreapi.Field(
#                 name='dish',
#                 location='form',
#                 required=True,
#                 schema=coreschema.Array(description='Список блюд')
#             )
#         ]


class CreateRestaurantSchema(AutoSchema):
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
                name='menus',
                location='form',
                required=True,
                schema=coreschema.Array(description='Меню')
            )
        ]


class UpdateRestaurantSchema(AutoSchema):
    def get_serializer_fields(self, path, method):
        return [
            coreapi.Field(
                name='id',
                location='form',
                required=True,
                schema=coreschema.String(description='id меняемой компании')
            ),
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
                name='menus',
                location='form',
                required=True,
                schema=coreschema.Array(description='Меню')
            )
        ]


class DeleteSchema(AutoSchema):
    def get_serializer_fields(self, path, method):
        return [
            coreapi.Field(
                name='id',
                location='form',
                required=True,
                schema=coreschema.String(description='id')
            )
        ]


# class CreateDishSchema(AutoSchema):
#     def get_serializer_fields(self, path, method):
#         return [
#             coreapi.Field(
#                 name='name',
#                 location='form',
#                 required=True,
#                 schema=coreschema.String(description='Название блюда')
#             ),
#             coreapi.Field(
#                 name='description',
#                 location='form',
#                 required=True,
#                 schema=coreschema.String(description='Описание блюда')
#             ),
#             coreapi.Field(
#                 name='price',
#                 location='form',
#                 required=True,
#                 schema=coreschema.Integer(description='Цена Блюда')
#             ),
#             coreapi.Field(
#                 name='price',
#                 location='form',
#                 required=True,
#                 schema=coreschema.(description='Цена Блюда')
#             )
#         ]
