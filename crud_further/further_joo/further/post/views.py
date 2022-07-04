import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import Post,Tag
# Create your views here.
class PostView(APIView):
    def post(self, request, post_id=None):
        author = request.user
        content = request.data.get('content','')
        tag_name_list = request.data.get('tags','')
        # tag_name_list = json.loads(request.data.get('tags',''))
        if content == '':
            return Response({
                "error" : "내용이 비어있습니다."
            })
        if tag_name_list == '':
            return Response({
                "error" : "태그가 비어있습니다."
            })
        tag_objects = []
        for tag_name in tag_name_list:
            tag_object, _ = Tag.objects.get_or_create(tag_name=tag_name)
            tag_objects.append(tag_object)
        new_post = Post.objects.create(
            author = author,
            content = content
        )
        new_post.tag.add(*tag_objects)
        new_post.save()
        return Response({
            "message" : "포스팅 완료"
        })
    def get(self, request, post_id=None):
        return Response(UserSerializer(request.user).data)
    def put(self, request, post_id):
        cur_post = Post.objects.get(id = post_id)
        cur_post.content = request.data.get('new_content')
        cur_post.save()
        return Response({
            "message" : "포스팅 수정완료"
        })
    def delete(self,request,post_id):
        cur_post = Post.objects.get(id = post_id)
        cur_post.delete()
        return Response({
            "message": "포스팅 삭제 완료"
        })