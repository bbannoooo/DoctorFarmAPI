from django.shortcuts import render
from Posts.models import Post
from Posts.serializers import PostSerializer
from rest_framework import viewsets
from Image.models import DetectedImageFile
from Image.serializers import DetectedImageFileSerializer
# Create your views here.

class Post_main(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        user = self.request.user
        image = DetectedImageFile.objects.filter(user=user)
        img_serializers = DetectedImageFileSerializer(image, many=True)
        img_url = 'detected/' + img_serializers.data[0]['image'].split('/')[-1]
        serializer.save(user = user, detected_image = img_url)
    
    def get_queryset(self):
        queryset = Post.objects.filter(is_public = True)
        return queryset

class Post_mypage(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user is not None and user != 'Anonymous':
            queryset = Post.objects.filter(user = user)
            return queryset