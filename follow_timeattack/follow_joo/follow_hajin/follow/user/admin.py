from django.contrib import admin

from . models import FollowModel, UserModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(FollowModel)