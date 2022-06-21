
from django.contrib.auth import login, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import UserModel
# Create your views here.
class UserView(APIView):
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        check_user = authenticate(request, username=username , password=password)
        if not check_user:
            return Response({
                "error": "존재하지 않는 계정이거나 패스워드가 틀렸습니다."
            })
        login(request, check_user)
        return Response({
            "message" : "로그인 성공"
        })
class UserSignUpView(APIView):
    def post(self,request):
        password = request.data.pop("password")
        new_user = UserModel.objects.create(
            **request.data
        )
        new_user.set_password(password)
        new_user.save()
        return Response({
            "message" : "회원가입성공"
        },status=status.HTTP_200_OK)