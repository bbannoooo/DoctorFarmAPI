from django.shortcuts import render
from Posts.models import Post
from Posts.serializers import PostSerializer
from rest_framework import viewsets
# Create your views here.

class Post_main(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class Post_mypage(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user is not None and user != 'Anonymous':
            queryset = Post.objects.filter(user = user)
            return queryset