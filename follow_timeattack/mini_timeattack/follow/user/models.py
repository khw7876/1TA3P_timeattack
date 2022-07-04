from django.conf import settings
from django.db import models

# Create your models here.
class User(models.Model):
    email = models.TextField(max_length=200)
    password = models.TextField(max_length=200)
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='followee')




