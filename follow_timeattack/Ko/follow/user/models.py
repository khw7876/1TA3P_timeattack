from pyexpat import model
import django
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user_table"
    follow = models.ManyToManyField('UserModel', related_name="followee")
