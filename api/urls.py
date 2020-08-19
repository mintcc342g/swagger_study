from django.urls import path
from django.conf import settings

from .views import *

urlpatterns = [
    path("v1/music", MusicViewSet.as_view({"get": "list", "post": "add"}), name="musics"),
    path("v1/music/<int:music_num>", MusicViewSet.as_view({"get": "list"}), name="music"),
    path("v1/music/no_body", MusicViewSet.as_view({"post": "add_for_no_body"}), name="no_body_test"),
    path("v1/play_list", PlayListViewSet.as_view({"get": "list", "post": "add"}), name="play_lists"),
    path("v1/play_list/<str:play_list_name>", PlayListViewSet.as_view({"get": "list"}), name="play_list"),
]
