from django.db import models

# Create your models here.
class PostModel(models.Model):
    author = models.ForeignKey("user.User", on_delete=models.CASCADE)
    contents = models.TextField("내용", max_length=200)

    def __str__(self):
        return f"{self.author}"
    
