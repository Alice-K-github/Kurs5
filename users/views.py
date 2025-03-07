from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView
from rest_framework_simplejwt.views import TokenObtainPairView

from users.forms import CustomUserCreationForm
from users.serializers import MyTokenObtainPairSerializer


class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('')


class CustomLogoutView(LogoutView):
    template_name = 'logout.html'
    success_url = reverse_lazy('')


class RegisterView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
