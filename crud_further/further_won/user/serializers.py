from rest_framework import serializers

from post.models import PostModel, TagModel
from .models import User as UserModel




class TagSerializer(serializers.ModelSerializer):
    # 같은 태그를 가진 post 불러오기
    same_tag_posts = serializers.SerializerMethodField()
    def get_same_tag_posts(self, obj):
        # same_tag_posts_user_dict = {}
        # for post in obj.postmodel_set.all():
        #     same_post_user={}
        #     same_post_user["same_tag_posts"] = post.contents
        #     same_post_user["same_tag_user"] = post.author.username
        # same_tag_posts_user_dict["total"] = same_post_user

        # return same_tag_posts_user_dict
        #return [post.contents for post in obj.postmodel_set.all()]
        return [{"same_tag_posts": post.contents, "same_tag_user": post.author.username} for post in obj.postmodel_set.all()]

    class Meta:
        model = TagModel
        fields = ["tag_name", "same_tag_posts"]


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = PostModel
        fields = ["contents", 'id', 'tags']

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