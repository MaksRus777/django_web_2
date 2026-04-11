from django.contrib import admin
from django.urls import path
from dj_app import views

urlpatterns = [

    # Маршрут 0: Админка
    path('admin/', admin.site.urls),

    # Маршрут 1: Главная страница
    path('', views.index, name="index"),

    # Маршрут 2: Операции с базой данных
    path('operation', views.operation, name="operation"),

]
