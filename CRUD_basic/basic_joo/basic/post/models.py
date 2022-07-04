from django.db import models
from user.models import UserModel
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
