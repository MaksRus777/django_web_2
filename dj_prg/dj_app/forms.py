from django import forms

# --- ПАРАМЕТРЫ при создании ПОЛЕЙ ---
# label - Название поля (пишется слева).
# help_text - Подсказка поля (пишется снизу).
# initial - Начальное значение поля (пишется внутри).
# required - Необязательное к заполнению поле (False).
# ТЕКСТ: min_length и max_length - Количество символов ОТ..ДО, которое можно ввести.
# ЧИСЛА: min_value и max_value - Вариант цифры ОТ..ДО, которое можно ввести.
# widget - Объект HTML на основе которого будет визуально построено поле: forms.Textarea() или forms.DateInput().
# path - Начальный путь от которого будет выбор дальнейшего файла.
# allow_folders - Рассматривать папки для выбора (True).
# recursive - Рассматривать файлы в подпапках (True).
# match - Регулярное выражение для фильтрации файлов (.html$)

# --- ТАБЛИЦА ЗАВИСИМОСТИ МЕЖДУ [ТИПОМ ДАННЫХ] И [ВНЕШНИМ ВИДОМ] [BootStrap] ---
# forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
# forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
# forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
# forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
# forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}))
# forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
# forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
# forms.FilePathField(widget=forms.Select(attrs={'class': 'form-control'}))
# forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}))
# forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))



# Создание формы №1 (Основные поля)
class UserForm(forms.Form):
    # 1. Поля [str, int, bool]
    name = forms.CharField(label="Имя", help_text="Введите имя", required=False, initial="Алексей", min_length=3, max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label="Возраст", help_text="Введите возраст", required=False, initial="25", min_value=1, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    flag = forms.BooleanField(label="Флаг", required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    comment = forms.CharField(label="Комментарий", required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    # 2. Поле [Выбор ОДНОГО строкового элемента из списка]
    choices = (("Данные", "Название"), ("Английский", "Английский"), ("Немецкий", "Немецкий"), ("Испанский", "Испанский"))
    ling = forms.ChoiceField(label="Выберите язык", required=False, choices=choices, widget=forms.Select(attrs={'class': 'form-select'}))
    # 3. Поле [Выбор МНОЖЕСТВА строковых элементов из списка]
    choices = (("Данные", "Название"), ("Англия", "Англия"), ("Германия", "Германия"), ("Испания", "Испания"))
    country = forms.MultipleChoiceField(label="Выберите страну", required=False, choices=choices, widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    # 4. Поле [Выбор файла (ИМЯ.РАСШИРЕНИЕ) из ОС]
    file_name = forms.FileField(label="Имя файла", required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    # 5. Поле [Выбор файла (ПОЛНЫЙ ПУТЬ) из ОС]
    file_path = forms.FilePathField(label="Путь к файлу", required=False, match=".py$", recursive=True, allow_folders=True, path=r"C:\Users\Teacher\Desktop\TeacherPython", widget=forms.Select(attrs={'class': 'form-control'}))


# Создание формы №1 (Форма авторизации)
class AuthorizationForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))