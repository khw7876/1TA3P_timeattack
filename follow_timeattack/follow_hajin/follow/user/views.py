
from django.shortcuts import render, redirect
from . models import UserModel,FollowModel
# Create your views here.

def home(requset):
    return render(requset,'login.html')


def login(requset):
    if requset.method =='GET':
        return render(requset,'login.html')
    if requset.method =='POST':
        username = requset.POST.get('username',None)
        password = requset.POST.get('password',None)
        user_search = UserModel.objects.get(username=username)
        if user_search.password == password:
            return redirect('follow')
    
def follow(request):
    follow = FollowModel.objects.get(username='hajin')
    fol = follow.follow
    print(fol)
    
    return render(request,'index.html',{'follow':follow, 'fol':fol})
    