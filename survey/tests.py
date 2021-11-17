from importlib import import_module

from django.conf import settings
from django.test import TestCase
from django.urls import resolve

from .views import index
from .models import Question, Choice, Case, Result, ResultSong, Song

# Web Framework Unit Test 작성법 확인
class RestTest(TestCase):

    def setUp(self):
        engine = import_module(settings.SESSION_ENGINE)
        store = engine.SessionStore()
        store.save()
        self.session = store
        self.client.cookies[settings.SESSION_COOKIE_NAME] = store.session_key

    @classmethod
    def setUpClass(cls):
        super(RestTest, cls).setUpClass()
        # Temp DB를 채우는 역할

        # 다른 설정 안해놨으므로 모든 case parameter: 기본값 50
        case = Case(pk=20)
        case.save()
        case = Case.objects.get(case_id=20)

        question = Question(pk=5)
        question.save()
        question_other = Question(pk=4)
        question_other.save()
        question_last = Question(pk=10)
        question_last.save()
        question = Question.objects.get(question_id=5)

        choices = Choice(question_id=question_other, choice_id='4c')
        choices.save()
        choices = Choice.objects.get(question_id=question_other)
        choice_last = Choice(question_id=question_last, choice_id='10b')
        choice_last.save()

        result_final = Result(pk=5)
        result_final.save()
        result_final = Result.objects.get(result_id=5)

        love_me = Song(pk=1, song_link='m5kOBOfoySA', song_title='LOVE ME')
        love_me.save()
        deja_vu = Song(pk=10, song_link='dx0VcSNWdBg', song_title='Dejavu')
        deja_vu.save()
        love_me = Song.objects.get(song_id=1)

        # 실제 DB 내용과는 조금 다르지만 이렇게 설정했을 때 잘 값이 이동하는지 확인
        result_one = ResultSong(result_id=result_final, song_id=love_me)
        result_one.save()
        result_two = ResultSong(result_id=result_final, song_id=deja_vu)
        result_two.save()
        result_all = ResultSong.objects.get(song_id=love_me)

    def test_index_resolve(self):
        found_page = resolve('/')
        self.assertEqual(found_page.func, index)

    def test_get_question_resolve(self):
        response = self.client.get('/questions/5')
        self.assertIn(b'<!DOCTYPE html>', response.content)
        self.assertIn(b'Q5', response.content)
        self.assertIn(b'</html>', response.content)

    def test_choice_post(self):
        session = self.session
        session['case_id'] = 20
        session.save()
        response = self.client.post('/choice', {'cid': '4c'})
        self.assertTrue(response.url == 'questions/5')

    def test_enter_result(self):
        session = self.session
        session['case_id'] = 20
        session.save()
        response = self.client.post('/choice', {'cid': '10b'})
        self.assertTrue(response.url == 'result')

    def test_get_result_resolve(self):
        session = self.session
        session['case_id'] = 20
        session.save()
        response = self.client.get('/result')
        self.assertIn(b'm5kOBOfoySA', response.content)
        self.assertIn(b'dx0VcSNWdBg', response.content)
