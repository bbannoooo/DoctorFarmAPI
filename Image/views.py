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
    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    # def get_queryset(self):
    #     email =self.kwargs['email']
    #     return ImageFile.objects.filter(email=email)
class DetectedImageFile_main(viewsets.ModelViewSet):
    queryset = DetectedImageFile.objects.all()
    serializer_class = DetectedImageFileSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)