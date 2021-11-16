from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from .views import index, questions, choice, result


class RestTest(TestCase):
    def test_index_resolve(self):
        found_page = resolve('/')
        self.assertEqual(found_page.func, index)
# 유닛테스트 적용을 올바르게 하려면 View와 그 외 Service 로직을 최대한 분리해야 한다.

#    def test_get_question_resolve(self):
#        response = self.client.get('/questions/5')
#        self.assertTrue(response.content.startswith(b'<html>'))
#        self.assertIn(b'Q5', response.content)
#        self.assertTrue(response.content.endswith(b'<html>'))

#    def test_choice_post(self):
#        response = self.client.post('/choice', '3c')
#        other_response = self.client.get('questions/4')
#        self.assertEqual(response.status_code, 200)
#        self.assertEqual(response, other_response)

#    def test_enter_result(self):
#        response = self.client.post('choice', '11b')
#        other_response = self.client.get('/result')
#        self.assertEqual(response.status_code, 200)
#        self.assertEqual(response, other_response)

#    def test_get_result_resolve(self):
#        session = self.get_session()
#        session['case_id'] = 20
#        session.save()
#        self.set_session_cookies(session)
#        request = HttpRequest()
#        request.session.save()
#        response = result(request)
#        self.assertIn(b'm5kOBOfoySA', response.content)
#        self.assertIn(
#            ('some-key', 'some-value'),
#            response.client.session.items())