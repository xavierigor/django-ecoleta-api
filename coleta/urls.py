from rest_framework import routers
from coleta import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'points', views.PointViewSet)
router.register(r'items', views.ItemViewSet)

urlpatterns = [
    path('', include(router.urls))
]
