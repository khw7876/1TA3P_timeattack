from django.shortcuts import render
from . models import User, Content
from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from user.serializers import UserSerializer

class Login_View(APIView):
    def post(self, request): 
        username = request.data.get('username', '') 
        password = request.data.get('password', '')
        user = authenticate(request, username= username, password = password) 
        if not user: 
            return Response({'error' : '존재하지 않는 계정이거나 패스워드가 일치하지 않습니다.'}, status= status.HTTP_401_UNAUTHORIZED) 
        login(request, user) 
        return Response({'message': '로그인 성공!'}, status=status.HTTP_200_OK) 

class Content_View(APIView):
    def get(self, request, id=None):
        user = request.user
        return Response(UserSerializer(user).data)

    def post(self, request, id=None):
        user = request.user 
        title = request.data.get('title', '') 
        content = request.data.get('content', '')
        post = Content(
            user = user,
            title = title,
            content = content,
            )
        post.save()
        print(title,content)
        return Response({'message': '작성 성공!'}, status=status.HTTP_200_OK) 

    def put(self, request, id=id):
        title = request.data.get('title', '') 
        content = request.data.get('content', '')
        Content.objects.filter(id=id).update(
            title = title,
            content = content,
        )
        return Response({'message': '수정 성공!'}, status=status.HTTP_200_OK) 

    def delete(self, request, id=id):
        delete_get = Content.objects.filter(id=id).delete()
        print(delete_get)
        return Response({'message': '삭제 성공!'}, status=status.HTTP_200_OK) 