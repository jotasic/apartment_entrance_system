from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.dooradminviews import DoorAdminViewSet
router = DefaultRouter()
router.register(r'doors', DoorAdminViewSet)

urlpatterns = [
    path('/', include(router.urls), name='door_admin'),
    
]
