from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from django.views import View
from drf_yasg.utils import swagger_auto_schema, no_body
from drf_yasg.inspectors.base import openapi

from .models import PlayList
from .serializers import PlayListSerializer, PlayListBodySerializer, PlayListQuerySerializer
# Create your views here.


class ApiViewSet(viewsets.GenericViewSet,
                mixins.ListModelMixin,
                View):

    serializer_class = PlayListSerializer

    @swagger_auto_schema(query_serializer=PlayListQuerySerializer,)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        music_num = self.kwargs.get("music_num", None)

        play_list = PlayList.objects.all()
        if music_num:
            play_list = PlayList.objects.filter(id=music_num)

        return play_list

    @swagger_auto_schema(
        request_body=PlayListBodySerializer,
        manual_parameters=[openapi.Parameter('header_test', openapi.IN_HEADER, description="a header for  test", type=openapi.TYPE_STRING)])
    def add(self, request):
        play_list = PlayList.objects.filter(**request.data)
        if play_list.exists():
            return Response(data={'result': 'the music already exists.'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        play_list_serializer = PlayListSerializer(data=request.data, partial=True)
        if not play_list_serializer.is_valid():
            return Response(data={'result': 'the input data is invalid.'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        play_list = play_list_serializer.save()

        return Response(PlayListSerializer(play_list).data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(request_body=no_body)
    def add_for_no_body(self, request):

        return Response(data={'result': 'this is test api for no_body'}, status=status.HTTP_201_CREATED)