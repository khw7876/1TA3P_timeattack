from gc import unfreeze
from django.shortcuts import redirect, render
from django.contrib import auth
from .models import UserModel
# Create your views here.


def home(request):
    return render(request, 'user/sign_in.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        login_user = auth.authenticate(request, username = username, password= password)
        if login_user:
            auth.login(request, login_user)
            return redirect('/user/follow')
        return redirect('/user/')
    print("실패")
    return redirect('/user/')


def follow(request):
    if request.method == "GET":
        user = UserModel.objects.all()
        my_follows = UserModel.objects.filter(followee = request.user).username
        un_follows = UserModel.objects.filter(followee = request.user).username.exists()

        context = {my_follows, un_follows}

        for us in user:
            print(us)
        return render(request, 'user/follow.html', context)

def click_follow(request, username):
    if request.moehod == "POST":
        clicked_user = 

    