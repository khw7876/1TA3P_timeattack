from dataclasses import field
from rest_framework import serializers
from user.models import User as UserModel
from post.models import Post as PostModel
from post.models import Tag as TagModel


class TagSerializer(serializers.ModelSerializer):
    same_tag_post = serializers.SerializerMethodField()
    def get_same_tag_post(self,obj):

        return [{"author" : post.user.username,"content":post.content} for post in obj.post_set.all()]
        #여기서 같은 태그를 제공
    class Meta:
        model = TagModel
        fields = ["name", "same_tag_post"]

class PostSerializer(serializers.ModelSerializer):
    tag_name = TagSerializer(many=True) 

    class Meta:
        model = PostModel
        fields = ["user", "content", "tag_name"]

class userSerializer(serializers.ModelSerializer):
    post = PostSerializer(many = True, source = "post_set")
    post_bymodel = serializers.SerializerMethodField()

    def get_post_bymodel(self, obj):
        return [post.content for post in obj.post_set.all()]

    class Meta:
        model = UserModel
        fields = ["username", "post", "post_bymodel"]
