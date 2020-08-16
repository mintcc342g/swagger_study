from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from django.views import View

from .models import PlayList
from .serializers import PlayListSerializer
# Create your views here.


class ApiViewSet(viewsets.GenericViewSet,
                mixins.ListModelMixin,
                View):
    
    serializer_class = PlayListSerializer

    def get_queryset(self):
        music_num = self.kwargs.get("music_num", None)

        play_list = PlayList.objects.all()
        if music_num:
            play_list = PlayList.objects.filter(id=music_num)
        
        return play_list    # get_queryset은 list 형태로 반환해줘야 알아서 시리얼라이즈 먹여서 내보내줌.
    
    def add(self, request):
        play_list = PlayList.objects.filter(**request.data)
        if play_list.exists():
            return Response(data={'result': 'the music already exists.'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        # PlayList.objects.create() 를 사용해도 되겠지만, 시리얼라이저가 있으니 시리얼라이저로 해보자.
        play_list_serializer = PlayListSerializer(data=request.data, partial=True)
        if not play_list_serializer.is_valid():
            return Response(data={'result': 'the input data is invalid.'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        play_list = play_list_serializer.save()

        return Response(PlayListSerializer(play_list).data, status=status.HTTP_201_CREATED)