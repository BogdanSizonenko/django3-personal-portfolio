from django.urls import path
from . import views #Точка для импорта views, потому что этот файл в той же папке что views.py

urlpatterns = [
    path ('', views.all_blogs, name='all_blogs'),
]