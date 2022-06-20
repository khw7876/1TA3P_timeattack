from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login_View.as_view()),
    path('content/<int:id>',views.Content_View.as_view()),

]