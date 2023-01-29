from django.shortcuts import render
from .models import Post


def index(request):
    template = 'posts/index.html'
    title = 'Yatube'
    text = 'Это главная страница проекта Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'text': text,
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)
# Create your views here.


def group_posts(request):
    template = 'posts/group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    title = 'Лев Толстой – зеркало русской революции'
    context = {
        'text': text,
        'title': title,
    }
    return render(request, template, context)
