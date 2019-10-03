import datetime as dt
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

class QuestionModeTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + dt.timedelta(days=30)
        future_question= Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)
    
    def test_was_published_recently_with_recent_question(self):
        time1 = timezone.now() - (dt.timedelta(days=1)- dt.timedelta(seconds=1))
        recent_question= Question(pub_date=time1)
        self.assertIs(recent_question.was_published_recently(),True)

    def test_was_published_recently_with_old_question(self):
        time2 = timezone.now() - dt.timedelta(days=1,seconds=1)
        old_question= Question(pub_date=time2)
        self.assertIs(old_question.was_published_recently(),False)

def create_question(question_text, days):
    """
    Create a question given a question_text and the number of days offset from now
    """
    time= timezone.now() - dt.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


        