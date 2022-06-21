from django.db import models
from user.models import User
# Create your models here.
class Content(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    tag_name = models.ManyToManyField('TagModel')
    
class TagModel(models.Model):
    tag_name = models.CharField(max_length=15)

