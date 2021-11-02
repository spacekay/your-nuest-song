import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Question
from .models import Choice
from .models import Song
from .models import Result
from .models import ResultSong
from .models import Case


def index(request):
    return render(request, 'index.html')


def get_parameter(request, param):
    data = {
        'cid': param,
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


def choice(request):
    cid = request.POST.get("cid")
    print(cid)
    choice_result = cid[len(cid)-1:]
    qid = int(cid[0:len(cid)-1])+1
    print(choice_result, qid)
    url = "questions/"+str(qid)
    if qid == 3:
        return HttpResponseRedirect('result')
    else:
        return HttpResponseRedirect(url)


def result(request):
    return render(request, 'survey/result.html')


def like():
    return None


def dislike():
    return None

