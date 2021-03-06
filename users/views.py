from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from django.shortcuts import redirect, render
from django.views import View

from users.forms import LoginForm


class LoginView(View):

    def get(self, request):
        error_messages = list()
        form = LoginForm()
        context = {
            'errors': error_messages,
            'form': form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        error_messages = list()
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append('Nombre de usuario o contraseña incorrecta')
            else:
                if user.is_active:
                    django_login(request, user)
                    url = request.GET.get('next', 'photos_home')
                    return redirect(url)
                else:
                    error_messages.append('El usuario no está activo')
        context = {
            'errors': error_messages,
            'form': form
        }
        return render(request, 'users/login.html', context)


class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated:
            django_logout(request)
        return redirect('photos_home')
