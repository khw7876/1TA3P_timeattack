from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('follow/', views.follow, name='follow'),
    path('click_user/<int:user_id>', views.click_user, name='click_user'),
]
