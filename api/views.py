from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from django.views import View
from drf_yasg.utils import swagger_auto_schema, no_body
from drf_yasg.inspectors.base import openapi
from django.http import Http404

from .models import PlayList
from .serializers import PlayListSerializer, PlayListBodySerializer, PlayListQuerySerializer
# Create your views here.


class ApiViewSet(viewsets.GenericViewSet,
                mixins.ListModelMixin,
                View):

    serializer_class = PlayListSerializer  # 이 클래스형 view 에서 사용할 시리얼라이저를 선언

    # get_queryset에 데코레이터를 붙이면 인식을 못 하기 때문에 list를 상속 받아서 구현했다.
    # get_queryset은 list() 에서 불리는 함수에 불과하다.
    # 실제 response 하는 메소드는 list 이기 때문에 list를 상속받아서 데코레이터를 붙여준다.
    @swagger_auto_schema(query_serializer=PlayListQuerySerializer,)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        conditions = {
            'id': self.kwargs.get("music_num", None),
            'title__contains': self.request.GET.get('title', None),
            'star_rating': self.request.GET.get('star_rating', None),
            'singer__contains': self.request.GET.get('singer', None),
            'category__in': [self.request.GET.get('category_'+str(i+1), None) for i in range(4)],
            'created_at__lte': self.request.GET.get('created_at', None),
        }
        conditions = {key: val for key, val in conditions.items() if val is not None}

        play_list = PlayList.objects.filter(**conditions)
        if not play_list.exists():
            raise Http404()

        return play_list

    @swagger_auto_schema(
        request_body=PlayListBodySerializer,
        manual_parameters=[openapi.Parameter('header_test', openapi.IN_HEADER, description="a header for  test", type=openapi.TYPE_STRING)])
    def add(self, request):
        play_list = PlayList.objects.filter(**request.data)
        if play_list.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        play_list_serializer = PlayListSerializer(data=request.data, partial=True)
        if not play_list_serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        play_list = play_list_serializer.save()

        return Response(PlayListSerializer(play_list).data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(request_body=no_body)    # request_body에 no_body를 넣어줌.
    def add_for_no_body(self, request):
        return Response(status=status.HTTP_201_CREATED)
