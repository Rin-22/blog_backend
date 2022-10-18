

from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.request import Request
from .serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from apps.account import serializers

User = get_user_model()

class RegistrationView(APIView):
    @swagger_auto_schema(request_body=UserRegistrationSerializer)
    def post(self, request: Request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(
                'Thanks for registration! Activate your via link in your mail',
                status=status.HTTP_201_CREATED
            )

#TODO: активация, смена пароля, удаление аккаунта, востонавление пароля
#TODO: подключить celery, redis
#TODO: исправить HTML