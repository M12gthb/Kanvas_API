from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import Account
from .serializers import Accountserializer
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt import views as jwt_views


class AccountView(CreateAPIView):
    queryset = Account.objects.all
    serializer_class = Accountserializer

    @extend_schema(
        operation_id="account_create",
        summary="Criação de usuário",
        description="Cria um novo usuário para a aplicação.",
        tags=["Accounts/"],
        request=Accountserializer,
        responses={201: Accountserializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class LoginView(jwt_views.TokenObtainPairView):
    @extend_schema(
        operation_id="account_login",
        summary="Criação de usuário",
        description="Cria um novo usuário para a aplicação.",
        tags=["Login/"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
