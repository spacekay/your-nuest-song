from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('questions/<qid>', views.questions, name='questions'),
    path('result', views.result, name='result'),
    path('like/<rid>', views.like, name='like'),
    path('dislike/<rid>', views.dislike, name='dislike'),
    path('choice', views.choice, name='choice')
]