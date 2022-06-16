from pyexpat import model
import django
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(AbstractUser):
    class Meta:
        db_table ="user"
    
    
class follow(models.Model):
    class Meta:
        db_table = "follow"
    follow_user = models.ManyToManyField(UserModel, related_name='followee_user')
