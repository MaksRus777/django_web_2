from django.shortcuts import render
from dj_app.forms import *


# Главная страница
def index(request):

    # ЛОГИКА 1. [Клиент Обновил Страницу] - Когда клиент хочет посмотреть
    if request.method == "GET":
        form1 = UserForm()
        form2 = AuthorizationForm()
        context = {"form1": form1, "form2": form2}
        return render(request, "index.html", context=context)

    # ЛОГИКА 2. [Клиент Нажал Кнопку Войти] - Когда клиент чтото хочет отправить
    if request.method == "POST":

        data = []  # Список с правильными данными из формы

        # Автоматически берем нужные поля
        for key, value in request.POST.items():
            if key != "csrfmiddlewaretoken" and key != "country" and key != "flag":
                data.append([key, value])

        # Вручную добавляем Поле множественного выбора (Страна)
        list_country = request.POST.getlist("country")
        data.insert(4, ["country", list_country])

        # Вручную добавляем Поле флага
        flag = True if request.POST.get("flag") == "on" else False
        data.insert(2, ["flag", flag])

        form1 = UserForm()
        form2 = AuthorizationForm()
        context = {"form1": form1, "form2": form2}
        return render(request, "index.html", context=context)

    return None  # Заглушка чтобы PEP 8 не ругался
