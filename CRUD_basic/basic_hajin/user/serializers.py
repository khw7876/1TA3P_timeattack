from rest_framework import serializers
from .models import User,Content


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ["title","content"]


class UserSerializer(serializers.ModelSerializer):

    content= serializers.SerializerMethodField()
    def get_content(self, obj):
        return [{"title":content.title,"content":content.content} for content in obj.content_set.all()]


    class Meta:
        model = User
        fields = ["username","password","content"] 
