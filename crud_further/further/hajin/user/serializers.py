from rest_framework import serializers

from post.models import PostModel
from .models import User as UserModel



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ["contents", 'id']

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