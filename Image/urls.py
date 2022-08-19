from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

app_name = 'image'

router = routers.DefaultRouter(trailing_slash=False)
router.register('', views.ImageFile_main)


urlpatterns = [
    path('image/', include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
