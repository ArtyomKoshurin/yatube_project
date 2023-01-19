from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('posts/group/<slug:posts_slug>/', views.group_posts),
]