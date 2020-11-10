import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Clearance

class ClearanceModelTests(TestCase):
    def test_recent_post_with_future_post(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = Clearance(date_posted=time)
        self.assertIs(future_post.recent_post(),False)

    def test_recent_post_with_old_post(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_post = Clearance(date_posted=time)
        self.assertIs(old_post.recent_post(),False)
    
    def test_recent_post_with_recent_post(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_post = Clearance(date_posted=time)
        self.assertIs(recent_post.recent_post(),True)

    """ def test_student_profile_exists(self):
        student_exists = Clearance(student=1)
        self.assertIs(student_exists, True) """ #creating a profile instance here is a problem for me.

    