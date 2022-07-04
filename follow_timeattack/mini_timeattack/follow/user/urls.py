# 1. follow라는 프로젝트를 만든다.
# 2. user라는 앱을 만든다. 
# 3. 유저 모델을 생성한다. 
# 4. 더미 유저를 생성한다. 3명 이상
# 5. 팔로우 페이지에 모든 유저, 내가 팔로우한 모든 유저 데이터를 보내준다.
# 6. 유저의 이름을 누르면 팔로우, 팔로우 취소가 되는 로직을 만든다.


from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path("<str:email>", views.follow, name="follow"),
]