from django.urls import path

from .views      import DoorSearchAPIView

urlpatterns = [
    path('/door', DoorSearchAPIView.as_view(), name='door_search_api'),
]