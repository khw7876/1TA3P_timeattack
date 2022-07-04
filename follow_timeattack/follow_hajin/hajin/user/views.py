from django.shortcuts import redirect, render
from django.contrib import auth
from .models import User
def login(request):
    if request.method =='GET':
        return render(request, 'login.html')

    if request.method =='POST':
        username = request.POST.get('username',"")
        password = request.POST.get('password' "")
        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request,user)
            return redirect('/follower')
        else:
            return redirect('/login')


def follow(request):
    user = request.user
    if user:
        followers = User.objects.filter(follwee=user)
        users = User.objects.all().exclude(id=user.id).exclude(id__in = followers)
        return render(request, 'main.html',{'users':users,'followers':followers})
    else:
        return redirect('/login')


def following(request, user_id):
    user = request.user
    click_user = User.objects.get(id=user_id)
    if user.follower.filter(id = click_user.id).exists():
        user.follower.remove(click_user)
    else:
        user.follower.add(click_user)
    return redirect('/follower')
