from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница. '
                         'Здесь ты можещь ознакомиться с основной '
                         'информацией о сервисе.'
                         'Ты <i>не можешь</i> получить правильные '
                         '<b>ответы</b>,<br> если у тебя нет '
                         'правильных <s>вопросов</s> запросов.'
    )
# Create your views here.
def group_posts(request, any_slug):
    return HttpResponse('Страница постов, отсортированных по группам')
