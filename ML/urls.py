from django.urls import path, include
from ML import views

app_name = 'ML'

urlpatterns = [
    path('', views.run),
]