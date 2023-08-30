from django.db import models


# Create your models here.


class Trainer(models.Model):
    department_options = (

        ('backend', 'BACKEND'),
        ('frontend', 'FRONTEND'),
        ('network', 'NETWORK')
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    department = models.CharField(max_length=40, choices=department_options)
    active = models.BooleanField(default=True)
    profile = models.ImageField(upload_to='profiles/', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
