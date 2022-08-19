from dataclasses import field
from .models import ImageFile, DetectedImageFile
from rest_framework import serializers

class ImageFileSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = ImageFile
        fields = '__all__'

class DetectedImageFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetectedImageFile
        field = '__all__'