from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from account.serializers import UserSerializer, TokenObtainPairSerializer


class TokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = TokenObtainPairSerializer


class AccountViewSet(GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def create_user(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            text_error = ''
            error_dict = {}
            for error in serializer.errors:
                elm_error = serializer.errors.get(error)
                if len(elm_error) > 0:
                    text_error += "{} \n".format(elm_error[0])
                    error_dict.update({error: elm_error[0]})
            return Response({"detail": text_error, "error": error_dict}, status=status.HTTP_400_BAD_REQUEST)

        token_data = {
            "email": request.data["email"],
            "password": request.data["password"]
        }
        token_serializer = TokenObtainPairSerializer(data=token_data)
        token_serializer.is_valid(raise_exception=True)
        return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)
