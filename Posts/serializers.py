from rest_framework import serializers
from Posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    detected_image = serializers.ImageField(use_url=True)
    solution_image = serializers.ImageField(required=False, use_url=True)

    class Meta:
        model = Post
        fields = '__all__'