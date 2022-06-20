from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from user.models import User as UserModel
from post.models import Post as PostModel
# Create your views here.
class Posting(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, post_id = None):
        return Response({"message" : "post의 get임다"})

    def post(self, request, post_id = None):
        user = request.user
        content = request.data.get('content', '')

        new_post = PostModel.objects.create(user=user, content=content)
        new_post.save()
        return Response({"meesage" : "게시물을 달았으"})
    
    def put(self, request, post_id):
        user = request.user
        new_content = request.data.get('content', '')
        # get뒤에는 추가로 사용을 못하니까 filter사용...?, 무조건 하나만 가져올 거면, get을 사용하는게 나음
        # new_post = PostModel.objects.filter(id=post_id).update(user=user, content=new_content)
        new_post = PostModel.objects.get(id=post_id)
        new_post.content = new_content
        new_post.save()
        #new_post.conent
        #update는 여러개를 한 번에 업데이트 할 때 사용, create를 사용해라.

        return Response({"message" : "업데이트 일걸..?"})

    def delete(self, request, post_id):
        PostModel.objects.get(id=post_id).delete()
        return Response({"message" : "delete 되었을걸...?"})
