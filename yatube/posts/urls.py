from django.urls import path
from . import views

app_name = 'posts'


urlpatterns = [
    path('', views.index, name='main_page'),
    path('group/<slug:any_slug>/', views.group_posts, name='group_posts'),
    path('group_list/', views.group_posts, name='group_list')
]
