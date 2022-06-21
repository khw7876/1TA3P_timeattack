from rest_framework import serializers
from post.models import Content,TagModel


class Tagserializers(serializers.ModelSerializer):
    tag_name = serializers.SerializerMethodField()
    def get_tag_name(self,obj):
        print(obj)
    class Meta:
        model = TagModel
        fields = ["tag_name"]

