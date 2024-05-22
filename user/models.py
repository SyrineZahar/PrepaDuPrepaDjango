from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomUser(models.Model):
    roles= [
        ('ADMIN','ADMIN '),
        ('STUDENT','STUDENT'),
        ('TEACHER','TEACHER'),
    ]

    user= models.OneToOneField(User,
        related_name='customUser',
        on_delete=models.SET_NULL,
        null=True
    )
    id=models.AutoField(primary_key=True)
    roles = models.CharField(max_length=7, choices=roles) 
    phone = models.CharField(max_length=8)
    def __str__(self):
        return self.user.username