from django.shortcuts import render
from rest_framework import viewsets
from Solutions.serializers import SolutionsSerializer
from Solutions.models import Solutions
# Create your views here.

class Solutions_main(viewsets.ModelViewSet):
    queryset = Solutions.objects.all()
    serializer_class = SolutionsSerializer

class Solutions_mypage(viewsets.ModelViewSet):
    queryset = Solutions.objects.all()
    serializer_class = SolutionsSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user is not None and user != 'Anonymous':
            queryset = Solutions.objects.filter(user = user)
            return queryset