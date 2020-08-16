from django.urls import path
from django.conf import settings

from .views import ApiViewSet

urlpatterns = [
    path("v1/play_list", ApiViewSet.as_view({'get': 'list', 'post': 'add'}), name="my_play_list"),
    path("v1/play_list/<int:music_num>", ApiViewSet.as_view({'get': 'list'}), name="my_play_list_music"),
]
