from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response


from post.models import Post as PostModel
from post.models import Tag as TagModel

from user.serializers import userSerializer
# Create your views here.
class Posting(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, post_id=None):
        return Response(userSerializer(request.user).data)

    def post(self, request, post_id = None):
        user = request.user
        content = request.data.get('content', '')
        tag_names = request.data.get('tag_names', '')
        
        tag_name_list = [TagModel.objects.get_or_create(name = tag_name)[0] for tag_name in tag_names]

        new_post = PostModel.objects.create(user=user, content=content)
        new_post.tag_name.add(*tag_name_list)
        new_post.save()
        return Response({"meesage" : "게시물을 달았으"})
    
    def put(self, request, post_id):
        new_content = request.data.get('content', '')
        new_post = PostModel.objects.get(id=post_id)
        new_post.content = new_content
        new_post.save()

        return Response({"message" : "업데이트 일걸..?"})

    def delete(self, request, post_id):
        PostModel.objects.get(id=post_id).delete()
        return Response({"message" : "delete 되었을걸...?"})
