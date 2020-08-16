from django.urls import path
from django.conf import settings

from .views import ApiViewSet

urlpatterns = [
    path("v1/play_list", ApiViewSet.as_view({'get': 'list', 'post': 'add'}), name="my_play_list"),
    path("v1/play_list/<int:music_num>", ApiViewSet.as_view({'get': 'list'}), name="my_play_list_music"),
    path("v1/play_list/no_body", ApiViewSet.as_view({'post': 'add_for_no_body'}), name="no_body_test"),
]
