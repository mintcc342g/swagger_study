from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from django.views import View
from .models import PlayList

# Create your views here.


class ApiViewSet(viewsets.GenericViewSet,
                mixins.ListModelMixin,
                View):
    
    serializer_class = None

    def get_queryset(self):
        music_num = self.kwargs.get("music_num", None)

        play_list = PlayList.objects.all()
        if music_num:
            play_list = PlayList.objects.filter(id=music_num)
        
        return play_list    # get_queryset은 list 형태로 반환해줘야 알아서 시리얼라이즈 먹여서 내보내줌.