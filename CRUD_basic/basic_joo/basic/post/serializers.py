from dataclasses import field
from rest_framework import serializers
from .models import Post
from user.models import UserModel

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =["content"]

class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, source = "post_set")
    class Meta:
        model = UserModel
        fields = ["username","posts"]
