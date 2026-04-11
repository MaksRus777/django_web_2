from django.shortcuts import render
from dj_app.forms import *  # Импорт всех ФОРМ
from dj_app.models import *  # Импорт всех МОДЕЛЕЙ


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


# Метод для работы с операциями БД
def operation(request):
    # ЛОГИКА 1. [Клиент Обновил Страницу] - Когда клиент хочет посмотреть
    if request.method == "GET":

        # 1. Прочитать какая кнопка была нажата для чтения (all / one / filter)
        button = request.GET.get("button")

        # 2. Прочитать какая кнопка была нажата для удаления (all / one / filter)
        button_delete_id = request.GET.get("delete", None)  # None - Дефолтные данные (если кнопка не нажата)
        button_update_id = request.GET.get("update", None)  # None - Дефолтные данные (если кнопка не нажата)
        print("button_delete_id={} button_update_id={}".format(button_delete_id, button_update_id))
        # ТУТ ПРОДОЛЖИТЬ ....

        # 3. Создание формы
        form = OperationsForm()

        # 4. Чтение из БД в зависимости какая кнопка была нажата
        person = None
        if button == "all":
            person = Person.objects.all()
        if button == "one":
            person = [Person.objects.get(pk=5)]
        if button == "filter":
            person = Person.objects.filter(age=30)
        if button == "exclude":
            person = Person.objects.exclude(age=30)

        # 5. Показать страницу
        context = {"FORM": form, "TABLE": person}
        return render(request, "operation.html", context=context)

    # ЛОГИКА 2. [Клиент Нажал Кнопку Войти] - Когда клиент чтото хочет отправить
    if request.method == "POST":

        # 1. Вытянули данные из формы
        pk = request.POST.get("pk")
        name = request.POST.get("name")
        age = request.POST.get("age")

        # 2. Записать данные в БД
        Person.objects.create(name=name, age=age)  # !!!

        # 3. Создание формы
        form = OperationsForm()

        # 4. Прочитать из БД всех людей
        person = Person.objects.all()

        # 5. Показать страницу
        context = {"FORM": form, "TABLE": person}
        return render(request, "operation.html", context=context)

        # !!! Исправить create подсветку

    return None  # Заглушка чтобы PEP 8 не ругался