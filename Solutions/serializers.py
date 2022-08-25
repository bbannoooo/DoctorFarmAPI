from Solutions.models import Solutions
from rest_framework import serializers

class SolutionsSerializer(serializers.ModelSerializer):
    pesticide_image = serializers.ImageField(required=False, use_url=True)
    class Meta:
        model = Solutions
        fields = '__all__'