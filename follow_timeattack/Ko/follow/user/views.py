from gc import unfreeze
from django.shortcuts import redirect, render
from django.contrib import auth
from .models import UserModel
# Create your views here.

def home(request):
    return render(request, 'user/sign_in.html')

def sign_in(request):
    if request.method =="GET":
        return render(request, 'user/sign_in.html')
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    login_user = auth.authenticate(request, username=username, password=password)
    if login_user:
        auth.login(request, login_user)
        return render (request, 'user/follow.html')
    return redirect('/user')

def follow(request):
    user = request.user
    if request.method == "GET":
        my_follows = UserModel.objects.filter(followee = user)
        not_follow_users = UserModel.objects.all().exclude(followee=user).exclude(id=user.id)

        return render(request, 'user/follow.html', {"my_follows" : my_follows, "not_follow_users" : not_follow_users})

def click_user(request, user_id):
    user = request.user
    clicked_user = UserModel.objects.get(id=user_id)
    #클릭한 유저의 id로 조회를 하는데,
    #그 유저의 followee에 내가 있는가.

    if user.follow.filter(id = clicked_user.id):
        user.follow.remove(clicked_user)
        return redirect('/user/follow')
    user.follow.add(clicked_user)
    return redirect('/user/follow')