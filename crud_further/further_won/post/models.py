from django.db import models

# Create your models here.

class TagModel(models.Model):
    tag_name = models.CharField("태그", max_length=30)
    def __str__(self):
        return f"{self.tag_name}"


class PostModel(models.Model):
    author = models.ForeignKey("user.User", on_delete=models.CASCADE)
    contents = models.TextField("내용", max_length=200)
    tags = models.ManyToManyField(TagModel)

    def __str__(self):
        return f"{self.author}"
    



