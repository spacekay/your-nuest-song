from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('questions/<qid>', views.questions, name='questions'),
    path('result', views.result, name='result'),
    path('like', views.like, name='like'),
    path('dislike', views.dislike, name='dislike'),
    path('choice', views.choice, name='choice')
]