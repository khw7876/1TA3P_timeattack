from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .models import PostModel , TagModel
from rest_framework import status

from .serializers import UserModelSerializer, PostModelSerializer

# Create your views here.
class PostView(APIView):
    # 글 조회
    def get(self, request):
        user = request.user
        serialized_user_data = UserModelSerializer(user).data
        return Response(serialized_user_data, status = status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        title = request.data.get('title', '') 
        contents = request.data.get('contents', '')
        tag_names = request.data.get('tag_name','')
        new_article = PostModel.objects.create(
            author = user,
            title = title,
            contents = contents
        )
        tag_name_lists = []
        for tag_name in tag_names:
            tag_object,_ = TagModel.objects.get_or_create(tag_names=tag_name)
            tag_name_lists.append(tag_object)
        new_article.tag_names.add(*tag_name_lists)
        new_article.save()
        return Response({"message":"글 작성 완료!"})

    def put(self, request, post_id):
        device = PostModel.objects.get(id=post_id)
        serializer = PostModelSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #return Response({"message":"글 수정하기"})

    def delete(self, request, post_id):
        article = PostModel.objects.get(id=post_id)
        article.delete()
        return Response({"message":"글 삭제하기"})


