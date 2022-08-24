from Solutions.models import Solutions
from rest_framework import serializers

class SolutionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solutions
        fields = '__all__'