from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Question
from .models import Choice
from .models import Song
from .models import Result
from .models import ResultSong
from .models import Parameter


def index(request):
    return render(request, 'index.html')


def questions():
    return None


def select():
    return None


def submit():
    return None


def result():
    return None


def like():
    return None


def dislike():
    return None