from django.shortcuts import render,redirect
from .models import User

# Create your views here.
def signup_view(request):
    if request.method == 'GET':
        return render(request, "signup.html")
    elif request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get("password", '')

        new_user = User.objects.create(email=email, password=password)
        redirect("login")

def login_view(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get("password", '')

        me = User.objects.get(email=email)
        users = User.objects.all().exclude(email=me.email)

        return render(request, "main.html", {"users":users})


def follow(request, email):
    if request.method == "POST":
        me = request.user
        click_user = User.objects.get(email=email) 
        if me in click_user.followee.all(): 
            click_user.followee.remove(request.user) 
        else: 
            click_user.followee.add(request.user) 

        follow = me.follow.all()
        unfollow = User.objects.all().exclude(follow=request.user.follow)

        return render(request, "main.html", {'follows':follow, 'unfollows': unfollow})
