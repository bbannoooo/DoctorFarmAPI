from django.shortcuts import render
from Posts.models import Post
from Posts.serializers import PostSerializer
from rest_framework import viewsets
# Create your views here.

class Post_main(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
