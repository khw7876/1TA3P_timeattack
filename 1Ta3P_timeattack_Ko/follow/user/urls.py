from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('follow/', views.follow, name='follow'),
    path('click_follow/<str : username>', views.click_follow, name="click_follow")
]
