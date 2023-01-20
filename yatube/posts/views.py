from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template = 'posts/index.html'
    return render(request, template)
# Create your views here.
def group_posts(request, any_slug):
    return HttpResponse('Страница постов, отсортированных по группам')
