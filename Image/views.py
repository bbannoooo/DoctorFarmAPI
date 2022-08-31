from django.shortcuts import render
from Image.models import ImageFile, DetectedImageFile
from Image.serializers import ImageFileSerializer, DetectedImageFileSerializer
from rest_framework import viewsets
# from rest_framework import permissions

class ImageFile_main(viewsets.ModelViewSet):
    queryset = ImageFile.objects.all()
    serializer_class = ImageFileSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        
class DetectedImageFile_main(viewsets.ModelViewSet):
    queryset = DetectedImageFile.objects.all()
    serializer_class = DetectedImageFileSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    
    def get_queryset(self):
        queryset = DetectedImageFile.objects.all()
        user = self.request.user
        if user is not None and user != 'Anonymous':
            queryset = DetectedImageFile.objects.filter(user = user)
        return queryset