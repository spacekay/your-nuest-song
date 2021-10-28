from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('questions/<qid>', views.questions, name='questions'),
    path('select', views.select, name='select'),
    path('result', views.result, name='result'),
    path('like', views.like, name='like'),
    path('dislike', views.dislike, name='dislike'),
    path('<str:param>/', views.get_parameter)
    path('choice/<str:param>', views.choice, name='choice')
]