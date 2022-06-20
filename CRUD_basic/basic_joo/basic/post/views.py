from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import Post
# Create your views here.
class PostView(APIView):
    def post(self, request, post_id=None):
        author = request.user
        content = request.data.get('content')
        new_post = Post.objects.create(
            author = author,
            content = content
        )
        new_post.save()
        return Response({
            "message" : "포스팅 완료"
        })
    def get(self, request, post_id=None):
        return Response(UserSerializer(request.user).data)
    def put(self, request, post_id):
        cur_post = Post.objects.get(id = post_id)
        cur_post.content = request.data.get('new_content')
        cur_post.save()
        return Response({
            "message" : "포스팅 수정완료"
        })
    def delete(self,request,post_id):
        cur_post = Post.objects.get(id = post_id)
        cur_post.delete()
        return Response({
            "message": "포스팅 삭제 완료"
        })