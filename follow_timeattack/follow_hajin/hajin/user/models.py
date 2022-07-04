from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Meta:
        db_table = "user_table"
    follower = models.ManyToManyField('User', related_name='follwee')

