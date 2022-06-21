from django.contrib import admin
from django.urls import path, include
from user import views
from post import views

urlpatterns = [
    path('posting', views.Posting.as_view(), name='Posting'),
    path('posting/<int:post_id>', views.Posting.as_view(), name='Posting'),
]