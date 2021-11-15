import json

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Question, Case, Choice, Song, ResultSong, Result


def index(request):
    cases = Case.objects.all()
    case_number = len(cases) + 3
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
    # choice_result = cid[len(cid)-1:]
    qid = int(cid[0:len(cid) - 1]) + 1
    case_number = request.session['case_id']
    if qid == 2:
        this_case = Case()
    else:
        this_case = Case.objects.get(case_id=case_number)
    this_choice = Choice.objects.get(choice_id=cid)
    this_case.e_i_para = this_case.e_i_para + this_choice.e_i_para
    this_case.n_s_para = this_case.n_s_para + this_choice.n_s_para
    this_case.f_t_para = this_case.f_t_para + this_choice.f_t_para
    this_case.p_j_para = this_case.p_j_para + this_choice.p_j_para
    this_case.save()
    url = "questions/" + str(qid)
    if qid == 11:
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
    # 테스트용. 순서대로 isfp enfp infp entp intp isfp esfp enfj infj
    if ei == 50 and ns == 50 and ft == 50 and pj == 50:
        result_number = 5
    elif ei > 50 and ft >= 50 and ns > 50 and pj >= 50:
        result_number = 1
    elif ei <= 50 and ft >= 50 and ns > 50 and pj >= 50:
        result_number = 2
    elif ei > 50 and ft < 50 and ns > 50 and pj >= 50:
        result_number = 3
    elif ei <= 50 and ft < 50 and ns > 50 and pj >= 50:
        result_number = 4
    elif ei <= 50 and ns <= 50 and ft >= 50 and pj >= 50:
        result_number = 5
    elif ei > 50 and ns <= 50 and ft >= 50 and pj >= 50:
        result_number = 6
    elif ei > 50 and ns > 50 and ft >= 50 and pj < 50:
        result_number = 7
    elif ei <= 50 and ns > 50 and ft >= 50 and pj < 50:
        result_number = 8
    elif ei > 50 and ns <= 50 and ft < 50 and pj >= 50:
        result_number = 9
    elif ei <= 50 and ns <= 50 and ft < 50 and pj >= 50:
        result_number = 10
    elif ei <= 50 and ns <= 50 and ft < 50 and pj < 50:
        result_number = 11
    elif ei > 50 and ns <= 50 and ft < 50 and pj < 50:
        result_number = 12
    elif ei <= 50 and ns <= 50 and ft >= 50 and pj < 50:
        result_number = 13
    elif ei > 50 and ns <= 50 and ft >= 50 and pj < 50:
        result_number = 14
    elif ei <= 50 and ns > 50 and ft < 50 and pj < 50:
        result_number = 15
    elif ei > 50 and ns > 50 and ft < 50 and pj < 50:
        result_number = 16
    else:
        return render(request, 'error.html')
    your_result = Result.objects.get(result_id=result_number)
    song_numbers = ResultSong.objects.filter(result_id=result_number).order_by('priority')
    your_song = []
    for number in song_numbers:
        song = Song.objects.get(song_title=number.song_id)
        your_song.append(song)
    context = {
        'result': your_result,
        'your_song': your_song,
        'case': this_case,
    }
    return render(request, 'survey/result.html', context)


def like():
    return None


def dislike():
    return None
