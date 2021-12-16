from django.urls import path
from .views import RegisterApiView, ActivationView, LoginApiView, LogoutApiView, ChangePasswordView, ResetPasswordView

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('login/', LoginApiView.as_view()),
    path('logout/', LogoutApiView.as_view()),
    path('password/change/', ChangePasswordView.as_view()),
    path('password/reset/', ResetPasswordView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationView.as_view(), name='activate_account'),
]