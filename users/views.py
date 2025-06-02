from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import UserForm
from django.contrib.auth.models import User

class UserRegisterView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/pages/register.html'
    success_url = reverse_lazy('login')

# view generica do django para login usuarios
class UserLoginView(LoginView):
    template_name = 'users/pages/login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    

# view generica do django para logout
class UserLogoutView(LogoutView):
    next_page = 'home'