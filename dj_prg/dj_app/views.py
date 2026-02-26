from django.shortcuts import render
from dj_app.forms import *


# Главная страница
def index(request):

    # ЛОГИКА 1. [Клиент Обновил Страницу] - Когда клиент хочет посмотреть
    if request.method == "GET":
        form = AuthorizationForm()
        context = {"form": form}
        return render(request, "index.html", context=context)

    # ЛОГИКА 2. [Клиент Нажал Кнопку Войти] - Когда клиент чтото хочет отправить
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email, password)

        form = AuthorizationForm()
        context = {"form": form, "email": email, "password": password}
        return render(request, "index.html", context=context)

        # Проверка формы !!!!
