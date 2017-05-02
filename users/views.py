from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from django.shortcuts import redirect, render

from users.forms import LoginForm


def login(request):
    error_messages = list()
    if request.method == 'POST':
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
    else:
        form = LoginForm()

    context = {
        'errors': error_messages,
        'form': form
    }
    return render(request, 'users/login.html', context)

def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
    return redirect('photos_home')
