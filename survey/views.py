import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader, RequestContext

from .models import Question, Case
from .models import Choice
from .models import Song
from .models import Result
from .models import ResultSong
# from .models import Case


def index(request):
    cases = Case.objects.all()
    case_number = len(cases)
    print(case_number)
    request.session['case_id'] = case_number
    return render(request, 'index.html')


def questions(request, qid):
    question = Question.objects.get(question_id=qid)
    choice_list = Choice.objects.filter(question_id=qid)
    context = {
        'question': question,
        'choices': choice_list,
    }
    return render(request, 'survey/question.html', context)


def choice(request):
    cid = request.POST.get("cid")
    print(cid)
    choice_result = cid[len(cid)-1:]
    qid = int(cid[0:len(cid)-1])+1
    print(choice_result, qid)
    case_number = request.session['case_id']
    print(case_number)
    this_case = Case.objects.get(case_id=case_number)
    this_choice = Choice.objects.get(choice_id=cid)
    print(this_choice.e_i_para, this_case.e_i_para)
    this_case.e_i_para = this_case.e_i_para + this_choice.e_i_para
    print(this_case.e_i_para)
    this_case.n_s_para = this_case.n_s_para + this_choice.n_s_para
    this_case.f_t_para = this_case.f_t_para + this_choice.f_t_para
    this_case.p_j_para = this_case.p_j_para + this_choice.p_j_para
    this_case.save()
    url = "questions/"+str(qid)
    if qid == 3:
        return HttpResponseRedirect('result')
    else:
        return HttpResponseRedirect(url)


def result(request):
    case_number = request.session['case_id']
    this_case = Case.objects.get(case_id=case_number)
    print(this_case, "도착~")
    ei = this_case.e_i_para
    ns = this_case.n_s_para
    ft = this_case.f_t_para
    pj = this_case.p_j_para
    result_number = 0
    # 테스트용. 순서대로 isfp enfp infp entp intp
    if ei == 50 and ns == 50 and ft == 50 and pj == 50:
        result_number = 2
    elif ei >= 50 and ft >= 50:
        print("여기?")
        result_number = 1
    elif ei < 50:
        result_number = 1
    elif ei >= 50 and ft < 50:
        result_number = 3
    else:
        result_number = 4
    your_result = Result.objects.get(result_id=result_number)
    song_numbers = ResultSong.objects.filter(result_id=result_number).order_by('priority')
    your_song = []
    for number in song_numbers:
        print(number)
        song = Song.objects.get(song_title=number.song_id)
        your_song.append(song)
    context = {
        'result': your_result,
        'your_song': your_song,
    }
    return render(request, 'survey/result.html', context)


def like():
    return None


def dislike():
    return None

