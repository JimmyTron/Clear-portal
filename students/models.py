from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from clear.models import Department, Course
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Adm_no =models.CharField(max_length=100)
    def __str__(self):
        return f'{self.user.username} Profile'

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
    student = models.ForeignKey(User, on_delete=models.CASCADE) #change to OneToOneField to only have one request per user

    def __str__(self):
        #return f'{self.student.profile.Adm_no, self.student.first_name, self.request}'
        return self.student.first_name +" "+ self.student.last_name+" "+ self.student.profile.Adm_no +" "+ self.request
