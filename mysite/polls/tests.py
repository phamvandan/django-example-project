from django.test import TestCase
from .models import Question
# Create your tests here.

class QuestionModuleTest(TestCase):
    def test1(self):
        q = Question()
        self.assertEqual(q.show_hello(), 'Hello my friend')
