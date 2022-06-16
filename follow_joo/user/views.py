from django.shortcuts import redirect, render
from .models import User
from django.contrib import auth
# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login_page.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    cur_user = auth.authenticate(request, username=username, password=password)
    auth.login(request,cur_user)
    return redirect('/follower')

def follower(request):
    if request.method == 'GET':
        cur_user = request.user
        followers = User.objects.filter(followee = cur_user)
        users = User.objects.all().exclude(id = cur_user.id).exclude(id__in = followers)
        return render(request, 'follow_page.html', {'users':users, 'followers': followers})
        
def follow(request, user_id):
    cur_user = request.user
    clicked_user = User.objects.get(id=user_id)
    if cur_user.follower.filter(id = clicked_user.id).exists():
        cur_user.follower.remove(clicked_user)
    else:
        cur_user.follower.add(clicked_user)
    return redirect('/follower')
