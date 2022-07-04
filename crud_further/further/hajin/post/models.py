from django.db import models

# Create your models here.
class TagModel(models.Model):
    # TAG_NAME_LIST = [
    #     ('D','day'),
    #     ('S','sports'),
    #     ('F','food'),
    #     ('N','news')
    # ]
    tag_names = models.CharField(max_length=20)

class PostModel(models.Model):
    author = models.ForeignKey("user.User", on_delete=models.CASCADE)
    contents = models.TextField("내용", max_length=200)
    title = models.CharField(max_length=30)
    tag_names = models.ManyToManyField(TagModel)
    def __str__(self):
        return f"{self.author}"

