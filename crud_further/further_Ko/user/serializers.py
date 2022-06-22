from dataclasses import field
from rest_framework import serializers

from post.models import PostModel
from post.models import Tag as TagModel
from .models import User as UserModel

class TagSerializer(serializers.ModelSerializer):
    same_post = serializers.SerializerMethodField()

    def get_same_post(self,obj):
        return [{"same_username" : obj.author.username, "same_post_content" : obj.contents} for obj in obj.postmodel_set.all()]
        
    class Meta:
        model = TagModel
        fields = ["name", "same_post"]

class PostSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many = True)
    class Meta:
        model = PostModel
        fields = ["contents", 'id', 'tag']

class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, source="postmodel_set")
    class Meta:
        model = UserModel
        fields = ["username", "join_date", "posts"]

# class PostSerializer(serializers.ModelSerializer):
#     user_posting = serializers.SerializerMethodField()
#     def get_user_posting(self, obj):
#         return [post.contents for post in obj.contents.all()]
#     class Meta:
#         model = PostModel
#         fields = ["user_posting", "id"]



# class UserSerializer(serializers.ModelSerializer):
#     #posts = PostSerializer(many=True, source="")
#     post_method = serializers.SerializerMethodField()
#     def get_post_method(self, obj):
#         return [post.contents for post in obj.postmodel_set.all()]
#     class Meta:
#         model = UserModel
#         fields = ["username", "join_date", "post_method"]