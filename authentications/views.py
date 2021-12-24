from django.shortcuts import render
from django.contrib.auth import get_user_model, logout

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from django.views import View

from .permissions import IsOwnerOnly
from .models import Profile
from .serializers import RegisterSerializer, LoginSerializer, ChangePasswordSerializer, ResetPasswordSerializer, \
    ProfileSerializers
from .email import activation_email_send, reset_email_send


User = get_user_model()


class RegisterApiView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()

            if user:
                activation_email_send(user)
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


class LogoutApiView(APIView):
    model = User

    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class ResetPasswordView(UpdateAPIView):
    serializer_class = ResetPasswordSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            new_password = serializer.create_temporary_password()
            email1 = serializer.validated_data['email']
            user = serializer.save(new_password, email1)
            if user:
                reset_email_send(user, new_password)
                return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileUserAPIView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializers
    queryset = Profile.objects.all()
    permission_classes = [IsOwnerOnly]
    lookup_field = "id"

    def list(self, request):
        user = request.user
        query = Profile.objects.all(user=user)
        serializer = ProfileSerializers(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
