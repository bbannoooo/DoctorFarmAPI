from django.urls import path, include
from Solutions import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register('', views.Solutions_main)


urlpatterns = [
    path('', include(router.urls)),
]