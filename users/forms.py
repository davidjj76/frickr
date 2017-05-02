from django import forms


class LoginForm(forms.Form):

    usr = forms.CharField(label='Nombre de usuario',
                          widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    pwd = forms.CharField(label='Password',
                          widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
