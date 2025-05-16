from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView

urlpatterns = [
    path('registrar/', UserRegisterView.as_view(), name='register'),
    path('entrar/', UserLoginView.as_view(), name='login'),
    path('sair/', UserLogoutView.as_view(), name='logout'),
]