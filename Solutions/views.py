from django.shortcuts import render
from rest_framework import viewsets
from Solutions.serializers import SolutionsSerializer
from .models import Solutions
# Create your views here.

class Solutions_main(viewsets.ModelViewSet):
    queryset = Solutions.objects.all()
    serializer_class = SolutionsSerializer