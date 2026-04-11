from django.shortcuts import render


# Главная страница
def index(request):
    context = {}
    return render(request, "index.html", context=context)