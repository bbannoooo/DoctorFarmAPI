from django.urls import path, include
from rest_framework import routers
from Posts.models import Post
from Posts.serializers import PostSerializer
from Posts import views

app_name = 'Posts'

router = routers.DefaultRouter(trailing_slash=False)
router.register('', views.Post_main)

urlpatterns = [
    path('',include(router.urls)),
]