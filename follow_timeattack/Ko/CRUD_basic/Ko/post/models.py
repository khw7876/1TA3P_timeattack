from django.db import models

# Create your models here.
class Post(models.Model):
    class Meta:
        db_table = "post"
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.name