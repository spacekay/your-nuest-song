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


def get_parameter(request, param):
    data = {
        'no': param,
    }
    return render(request, 'survey/question.html', data)


def questions(request, qid):
    question = Question.objects.get(question_id=qid)
    choice_list = Choice.objects.filter(question_id=qid)
    context = {
        'question': question,
        'choices': choice_list,
    }
    return render(request, 'survey/question.html', context)


def select():
    return None


def submit():
    return None


def result(request):
    return render(request, 'survey/result.html')


def like():
    return None


def dislike():
    return None


