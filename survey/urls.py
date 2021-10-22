from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('questions', views.questions, name='questions'),
    path('select', views.select, name='select'),
    path('submit', views.submit, name='submit'),
    path('result', views.result, name='result'),
    path('like', views.like, name='like'),
    path('dislike', views.dislike, name='dislike'),
]