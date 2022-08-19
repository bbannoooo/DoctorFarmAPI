from django.urls import path, include
from . import views

app_name = 'ML'

urlpatterns = [
    path('', views.run),
]