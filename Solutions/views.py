from django.shortcuts import render
from rest_framework import viewsets
from Solutions.serializers import SolutionsSerializer, CodeSerializer, PesticideSerializer
from Solutions.models import Solutions, Code, Pesticide
# Create your views here.

class Solutions_main(viewsets.ModelViewSet):
    queryset = Solutions.objects.all()
    serializer_class = SolutionsSerializer

class Code_main(viewsets.ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer

class Pesticide_main(viewsets.ModelViewSet):
    queryset = Pesticide.objects.all()
    serializer_class = PesticideSerializer