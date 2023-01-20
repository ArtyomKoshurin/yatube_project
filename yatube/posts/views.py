from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    templates = 'posts/index.html'
    return render(request, templates)
# Create your views here.
def group_posts(request, any_slug):
    return HttpResponse('Страница постов, отсортированных по группам')
