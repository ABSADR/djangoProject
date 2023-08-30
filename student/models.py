from django.contrib.auth.models import User
from django.db import models
from django.db.models import TextField
from django.forms import DateTimeField

from trainer.models import Trainer


# Create your models here.

class Student(models.Model):

    gender_options = (

        ('male','MALE'),
        ('female','FEMALE')

    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    description = models.TextField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)
    gender = models.CharField(max_length=6, choices=gender_options)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    profile = models.ImageField(upload_to='profiles_student/', null=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name}{self.last_name}'


class HistoryStudent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=500)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.message