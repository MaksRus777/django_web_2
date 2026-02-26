from django import forms



from django import forms

# Форма авторизации
class AuthorizationForm(forms.Form):
    email = forms.CharField(label="Почта", required=True)
    password = forms.CharField(label="Пароль", required=True, widget=forms.PasswordInput)
