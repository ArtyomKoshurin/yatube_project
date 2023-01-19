from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница. '
                         'Здесь вы можете ознакомиться с основной '
                         'информацией о сервисе.')
# Create your views here.
def group_posts(request):
    return HttpResponse('Здесь будут находиться посты, '
                         'отфильтрованные по группам.')
