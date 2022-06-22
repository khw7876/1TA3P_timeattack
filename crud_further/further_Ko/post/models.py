from django.db import models

# Create your models here.

class Tag(models.Model):
    class Meta:
        db_table = "tag"
    name = models.CharField("태그이름", max_length=20)

    def __str__(self):
        return f"{self.name}"

class PostModel(models.Model):
    class Meta:
        db_table = "postmodel"
    author = models.ForeignKey("user.User", on_delete=models.CASCADE)
    contents = models.TextField("내용", max_length=200)
    tag = models.ManyToManyField(Tag, verbose_name="태그")

    def __str__(self):
        return f"{self.author}"
    
