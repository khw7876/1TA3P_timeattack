from dataclasses import field
from rest_framework import serializers
from .models import Post,Tag
from user.models import UserModel

class TagSerializer(serializers.ModelSerializer):
    same_tag_posts = serializers.SerializerMethodField()
    def get_same_tag_posts(self,obj):
        same_post = [{
            "author":post.author.username,
            "content" : post.content
        } for post in obj.post_set.all()]
        return same_post
    class Meta:
        model = Tag
        fields = ['tag_name','same_tag_posts']

class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, source='tag')
    
    class Meta:
        model = Post
        fields =["content", 'tags']

class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, source = "post_set")
    class Meta:
        model = UserModel
        fields = ["username","posts"]
