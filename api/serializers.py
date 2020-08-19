from .models import *
from rest_framework import serializers

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        music = Music.objects.all()
        model = Music
        fields = '__all__'  # __all__ 을 줄 경우, 모든 필드가 사용됨.
        # fields = ('id', 'created_at', 'title', 'category', 'star_rating',)  # 필드(컬럼)를 직접 명시하면, 명시된 필드만 사용됨. response에서는 선언한 순서가 빠른 필드가 더 위에 나옴.


class MusicBodySerializer(serializers.Serializer):
    singer = serializers.CharField(help_text="가수명")
    title = serializers.CharField(help_text="곡 제목")
    category = serializers.ChoiceField(help_text="곡 범주", choices=('JPOP', 'POP', 'CLASSIC', 'ETC'))
    star_rating = serializers.IntegerField(help_text="1~3 이내 지정 가능. 숫자가 클수록 좋아하는 곡")


class MusicQuerySerializer(serializers.Serializer):
    title = serializers.CharField(help_text="곡 제목으로 검색", required=False)
    star_rating = serializers.ChoiceField(help_text="곡 선호도로 검색", choices=(1, 2, 3), required=False)
    singer = serializers.CharField(help_text="가수명으로 검색", required=True)
    category_1 = serializers.ChoiceField(help_text="카테고리로 검색", choices=('JPOP', 'POP', 'CLASSIC', 'ETC'), required=False)
    category_2 = serializers.ChoiceField(help_text="카테고리로 검색", choices=('JPOP', 'POP', 'CLASSIC', 'ETC'), required=False)
    category_3 = serializers.ChoiceField(help_text="카테고리로 검색", choices=('JPOP', 'POP', 'CLASSIC', 'ETC'), required=False)
    category_4 = serializers.ChoiceField(help_text="카테고리로 검색", choices=('JPOP', 'POP', 'CLASSIC', 'ETC'), required=False)
    created_at = serializers.DateTimeField(help_text="입력한 날짜를 기준으로 그 이전에 추가된 곡들을 검색", required=False)


class MusicForPlayListSerializer(serializers.ModelSerializer):
    class Meta:
        music = Music.objects.all()
        model = Music
        fields = ('singer', 'title', 'category', 'star_rating',)


class PlayListSerializer(serializers.ModelSerializer):
    # 만약 get_queryset을 사용하고 관계가 있는 모델을 사용할 경우,
    # 시리얼라이저의 필드명은 모델에서 선언한 필드명과 동일하게 써줘야 함.
    # 안 그러면 response 값에 시리얼라이저가 안 먹혀서 해당 필드는 안 보이게 됨.
    music = MusicForPlayListSerializer(read_only=True)
    # music = MusicSerializer(read_only=True)  # Music의 모든 필드를 보이고 싶다면 이 시리얼라이저를 사용하면 됨.

    class Meta:
        play_list = PlayList.objects.all()
        model = PlayList
        fields = ('play_list_name', 'created_at', 'updated_at','music',) # 원하는 필드만 선언할 때, 관계가 있는 모델의 필드명을 써준다.


class PlayListQuerySerializer(serializers.Serializer):
    title = serializers.CharField(help_text="곡 제목으로 검색", required=False)
    singer = serializers.CharField(help_text="가수명으로 검색", required=False)


class PlayListBodySerializer(serializers.Serializer):
    name = serializers.CharField(help_text="플레이 리스트 이름")
    play_list = MusicBodySerializer(read_only=True)