from django.urls import path
from django.conf import settings

from .views import ApiViewSet

api_view_set = ApiViewSet.as_view({
    'get': 'list',
    'post': 'add'
})

urlpatterns = [
    path("v1/play_list", api_view_set, name="my_play_list"),
    path("v1/play_list/<int:music_num>", api_view_set, name="my_play_list"),
]