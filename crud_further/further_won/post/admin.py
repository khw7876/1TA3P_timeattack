from django.contrib import admin
from .models import PostModel, TagModel

# Register your models here.
admin.site.register(PostModel)
admin.site.register(TagModel)