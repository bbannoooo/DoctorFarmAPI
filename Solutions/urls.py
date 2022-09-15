from django.urls import path, include
from Solutions import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register('', views.Solutions_main)
router.register('code/', views.Code_main)
router.register('pesticide/', views.Pesticide_main)

# router2 = routers.DefaultRouter(trailing_slash=False)
# router2.register('', views.Code_main)

# router3 = routers.DefaultRouter(trailing_slash=False)
# router3.register('', views.Pesticide_main)

urlpatterns = [
    path('', include(router.urls)),
    # path('code/', include(router2.urls)),
    # path('pesticide/', include(router3.urls))
]