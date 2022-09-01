from django.urls import path, include
from rest_framework import routers
from Posts.models import Post
from Posts.serializers import PostSerializer
from Posts import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Posts'

router = routers.DefaultRouter(trailing_slash=False)
router.register('', views.Post_main)

router2 = routers.DefaultRouter(trailing_slash=False)
router2.register('', views.Post_mypage)

urlpatterns = [
    path('solutions/', include(router.urls)),
    path('mypage/', include(router2.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)