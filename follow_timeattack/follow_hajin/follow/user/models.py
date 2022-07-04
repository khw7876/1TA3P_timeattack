from django.db import models


# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=120)

class FollowModel(models.Model):
    username =  models.CharField(max_length=256)
    follow = models.ManyToManyField(UserModel)