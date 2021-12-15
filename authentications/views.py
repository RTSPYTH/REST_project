from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views import View
from rest_framework_simplejwt.views import TokenObtainPairView

from authentications.serializers import RegisterSerializer, LoginSerializer
from authentications.email import email_send

User = get_user_model()


class RegisterApiView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()

            if user:
                email_send(user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)


class ActivationView(View):

    def get(self, request, activation_code):

        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return render(request, 'index.html', {})

        except User.DoesNotExist:
            return render(request, 'link_exp.html', {})


class LoginApiView(TokenObtainPairView):
    serializer_class = LoginSerializer