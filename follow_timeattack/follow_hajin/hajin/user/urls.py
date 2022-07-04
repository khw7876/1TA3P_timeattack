from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('follower/', views.follow, name='follower'),
    path('following/<int:user_id>', views.following, name='following')
]