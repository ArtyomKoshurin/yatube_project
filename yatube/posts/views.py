from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница. '
                         'Здесь вы можете ознакомиться с основной '
                         'информацией о сервисе.')
# Create your views here.
def group_posts(request, slug):
    return HttpResponse(f'Страница, на которой будут посты, '
                        f'отсортированные по группам. {slug}')
