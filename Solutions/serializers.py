from Solutions.models import Solutions, Code, Pesticide
from rest_framework import serializers

class SolutionsSerializer(serializers.ModelSerializer):
    # pesticide_image = serializers.ImageField(required=False, use_url=True)
    class Meta:
        model = Solutions
        fields = '__all__'

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = '__all__'

class PesticideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesticide
        fields = '__all__'