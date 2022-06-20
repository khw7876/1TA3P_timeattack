from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout

from .serializers import userSerializer
# Create your views here.

class Home(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]
    def get(self,request):
        return Response(userSerializer(request.user).data)


class Login(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({"message" : "get방식임다"})
    
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password = password)
        if user:
            login(request,user)
            return Response({"message" : "로그인 돼쓰"})
        return Response({"message" : "뭔가 문제가 있겄지,,"})
    
    def put(self, request):

        return Response({"message" : "put방식임다"})

    def delete(self, request):

        return Response({"message" : "delete방식임다"})