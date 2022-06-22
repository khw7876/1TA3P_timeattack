from django.contrib import admin
from .models import PostModel, Tag

# Register your models here.
admin.site.register(PostModel)
admin.site.register(Tag)