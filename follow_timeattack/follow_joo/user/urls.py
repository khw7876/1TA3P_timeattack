from django.urls import path
from . import views
urlpatterns = [
    path('', views.login, name='login'),
    path('follower', views.follower, name='follower'),
    path('follow/<int:user_id>', views.follow, name='follow')
]
