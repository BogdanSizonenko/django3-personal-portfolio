from django.shortcuts import render
from django.http import HttpResponse
from .models import Project # Импортируем модель проекта

def home(request):
    projects = Project.objects.all() # Импортируем все записи о проектах из базы данных
    return render(request, 'portfolio/home.html', {'projects':projects} ) # Используя переменную projects, передаем словарь в шаблом с ключем projects и значением: список projects выше
def about(request):
    return render (request, 'portfolio/about.html')
