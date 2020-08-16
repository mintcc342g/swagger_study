from django.urls import path
from django.conf import settings

from .views import ApiViewSet

api_view_set = ApiViewSet.as_view({
    'get': 'list',  # 간단한 app 이므로 한 함수 내에서 음악목록과 음악 1개를 가져오는 걸 전부 처리하는 걸로 함..
    'post': 'add'
})

urlpatterns = [
    path("v1/play_list", api_view_set, name="my_play_list"),
    path("v1/play_list/<int:music_num>", api_view_set, name="my_play_list"),
]