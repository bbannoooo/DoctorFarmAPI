from .models import ImageFile, DetectedImageFile
from rest_framework import serializers

class ImageFileSerializer(serializers.ModelSerializer):
    # use_url 을 True 로 선언해 주면 output으로 URL String 이 내려오고 False 이면 File Name 이 output 으로 나온다.
    # Default 값은 UPLOADED_FILES_USE_URL 로 set 되어 있는데, 따로 설정안한다면 이 값은 True 값을 가지고 있다.
    image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = ImageFile
        fields = '__all__'

class DetectedImageFileSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, use_url=True)
    class Meta:
        model = DetectedImageFile
        fields = '__all__'