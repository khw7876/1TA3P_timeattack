from django.db import models

# Create your models here.

class Tag(models.Model):
    class Meta:
        db_table ="tag"
    name = models.CharField('태그이름', max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    class Meta:
        db_table = "post"
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    content = models.TextField()
    tag_name = models.ManyToManyField(Tag, verbose_name="태그")
    def __str__(self):
        return self.content


