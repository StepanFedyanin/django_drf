from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from server.account.models import User
from server.account.schemas import CreateCodePhoneSchema, PostCodePhoneSchema
from server.account.serializers import UserSerializer, UserTokenObtainPairSerializer
from rest_framework.generics import get_object_or_404


class TokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = UserTokenObtainPairSerializer


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
        token_serializer = UserTokenObtainPairSerializer(data=token_data)
        token_serializer.is_valid(raise_exception=True)
        return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)


class LoginWithPhoneViewSet(GenericViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'], schema=CreateCodePhoneSchema())
    def create_code(self,request):
        users = User.objects.all()
        user = get_object_or_404(users, phone=request.data['phone'])
        return Response({'code': 'sent'}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], schema=PostCodePhoneSchema())
    def post_code(self, request):
        users = User.objects.all()
        user = get_object_or_404(users, phone=request.data['phone'])
        if user.code == request.data['code']:

            token = user._generate_jwt_token()
            return Response(token, status=status.HTTP_201_CREATED)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
