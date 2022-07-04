from django.contrib import admin
from .models import Content, TagModel

# Register your models here.
admin.site.register(Content)
admin.site.register(TagModel)