from rest_framework import serializers

from post.models import PostModel,TagModel
from user.models import User as UserModel

class TagModelserializer(serializers.ModelSerializer):
    same_tag_post = serializers.SerializerMethodField()
    def get_same_tag_post(self, obj):
        print()
        same_post = [{
            "author":postmodel.author.username,
            "content" : postmodel.contents
        } for postmodel in obj.postmodel_set.all()]

        # 1. obj 을 통해 TagModel object 를 가져온다.
        # 2. obj.postmodel_set.all()으로 역참조를 해서 postmodel의 객체를 쿼리셋으로 모두 가져 온다. 
        # (post -> tag 정참조) (tag -> post) 역참조 tag에는 tag_names 라는 필드밖에 없으니.
        # 3. 원하는 데이터만 출력하기위해 리스트 컴프리헨션 을 이용해서 최종출력값 => 
        # "author":postmodel.author.username, "content":postmodel.contetns 라는 값만 가져온다
        # postmodel => (쿼리셋=obj.postmodel_set.all()).contes
        # postmodel => (쿼리셋=obj.postmodel_set.all()).author.username 
        # author.username 은 postmodel에 .author를 조회하면 Usermodel과의 포링키 이기 때문에
        # .username 을 통해서 조회한다(정참조.)
        return same_post

    class Meta:
        model = TagModel
        fields = ['tag_names',"same_tag_post"]

class PostModelSerializer(serializers.ModelSerializer):
    tag_names = TagModelserializer(many=True)
    class Meta:
        model = PostModel
        fields = ["author", 'title',"contents","tag_names"]

class UserModelSerializer(serializers.ModelSerializer):
    posts = PostModelSerializer(many=True, source="postmodel_set")
    class Meta:
        model = UserModel
        fields = ["username", "join_date", "posts"]        