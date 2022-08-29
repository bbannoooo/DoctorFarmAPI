from rest_framework import serializers
from Posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    detected_image = serializers.ImageField(required=False, use_url=True)
    solution_image = serializers.ImageField(required=False, use_url=True)
    email = serializers.ReadOnlyField(source = 'user.email')
    
    class Meta:
        model = Post
        fields = '__all__'