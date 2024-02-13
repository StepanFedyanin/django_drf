import coreapi
import coreschema
from rest_framework.schemas import AutoSchema


class CreateCodePhoneSchema(AutoSchema):
    def get_serializer_fields(self, path, method):
        return [
            coreapi.Field(
                name='phone',
                location='form',
                required=True,
                schema=coreschema.String(description='Номер телефона')
            )
        ]


class PostCodePhoneSchema(AutoSchema):
    def get_serializer_fields(self, path, method):
        return [
            coreapi.Field(
                name='phone',
                location='form',
                required=True,
                schema=coreschema.String(description='Номер телефона')
            ),
            coreapi.Field(
                name='code',
                location='form',
                required=True,
                schema=coreschema.String(description='смс код')
            )
        ]
