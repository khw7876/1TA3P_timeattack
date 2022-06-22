from django.shortcuts import render
from rest_framework.response import Response
# permission을 사용하기 위함
from rest_framework.views import APIView 
from rest_framework import permissions
from rest_framework import status

# Create your views here.
from django.contrib.auth import login, logout, authenticate

class UserApiView(APIView):
    # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(request, username=username, password=password)
		# user 객체가 들어가거나 None
        if not user: # None일때!
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)
        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)

	# 로그아웃
    def delete(self, request):
        logout(request)
        return Response({"message": "logout success!!"})