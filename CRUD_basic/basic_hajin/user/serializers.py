from rest_framework import serializers
from post.serializers import Tagserializers
from .models import User
from post.models import Content,TagModel



class Tagserialzier(serializers.ModelSerializer):
    same_tag_post = serializers.SerializerMethodField()
    def get_same_tag_post(self,obj):
        return[{"title":same_tag_post.title,"user":same_tag_post.user.username} for same_tag_post in obj.content_set.all()]    
            
    class Meta:
        model = TagModel
        fields = ["tag_name","same_tag_post"]

class Contentserializer(serializers.ModelSerializer):
    tag_name = Tagserialzier(many=True)
    class Meta: 
        model = Content
        fields = ["content","tag_name"]

class UserSerializer(serializers.ModelSerializer):
    content_set = Contentserializer(many=True)
    class Meta:
        model = User
        fields = ["username","content_set"] 
