from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from department.models import Department, Course
from PIL import Image
import datetime
CLEARANCE_CHOICES = [
    ('PENDING', 'Pending'),
    ('APPROVED', 'Approved'),
    ('DECLINED', 'Declined'),
    ('REVISED', 'Revised'),
]
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Adm_no =models.CharField(max_length=100)
    def __str__(self):
        return f'{self.user.first_name +" "+self.user.last_name}'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Clearance(models.Model):
    request = models.CharField(default="Clearance Request", max_length=100)
    departments = models.ManyToManyField(Department)
    date_posted = models.DateTimeField(default=timezone.now)
    student = models.OneToOneField(StudentProfile, on_delete=models.CASCADE) #change to OneToOneField to only have one request per user
    cleared = models.BooleanField(default=False)

    def recent_post(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_posted <=now 
        """ return self.date_posted >= timezone.now() - datetime.timedelta(days=1) 'failing test' """

    def __str__(self):
        #return f'{self.student.Adm_no, self.student.user.first_name, self.request}'
        return self.student.user.first_name +" "+ self.student.user.last_name+" "+ self.student.Adm_no +" "+ self.request
""" The f string version inserts brackets and apostrophes to the return string"""

"""def post_save_profile_create(sender, instance, created, *args, **kwargs):
    studentprofile, created = StudentProfile.objects.get_or_create(user=instance)

post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)"""
