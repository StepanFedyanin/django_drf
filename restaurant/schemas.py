from rest_framework.schemas import AutoSchema, coreapi


class PromoSchema(AutoSchema):

    def get_serializer_fields(self, path, method, coreschema=None):
        return [
                coreapi.Field(
                    name='promo_code',
                    location='form',
                    required=True,
                    schema=coreschema.String(description='Промокод')
                )
        ]