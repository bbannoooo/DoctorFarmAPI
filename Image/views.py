from django.shortcuts import render
from .models import ImageFile
from .serializers import ImageFileSerializer
from rest_framework import viewsets
# from rest_framework import permissions

class ImageFile_main(viewsets.ModelViewSet):
    queryset = ImageFile.objects.all()
    serializer_class = ImageFileSerializer

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    # def get_queryset(self):
    #     email =self.kwargs['email']
    #     return ImageFile.objects.filter(email=email)