from rest_framework import serializers
from user.models import User as UserModel
from post.models import Post as PostModel

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ["content"]

class userSerializer(serializers.ModelSerializer):
    post = PostSerializer(many = True, source = "post_set")
    post_bymodel = serializers.SerializerMethodField()

    def get_post_bymodel(self, obj):
        return [post.content for post in obj.post_set.all()]

    class Meta:
        model = UserModel
        fields = ["username", "post", "post_bymodel"]
