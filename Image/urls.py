from django.urls import path, include
from Image import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

app_name = 'image'

router_image = routers.DefaultRouter(trailing_slash=False)
router_image.register('', views.ImageFile_main)

router_detected_image = routers.DefaultRouter(trailing_slash=False)
router_detected_image.register('', views.DetectedImageFile_main)

urlpatterns = [
    path('image/', include(router_image.urls)),
    path('detected_image/', include(router_detected_image.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
