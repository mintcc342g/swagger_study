from .models import PlayList
from rest_framework import serializers

class PlayListSerializer(serializers.ModelSerializer):
    class Meta:
        play_list = PlayList.objects.all()
        model = PlayList
        fields = '__all__'  # __all__ 을 줄 경우, 모든 필드가 사용됨.
        # fields = ('id', 'created_at', 'title', 'category', 'star_rating',)  # 필드(컬럼)를 직접 명시하면, 명시된 필드만 사용됨.


class PlayListBodySerializer(serializers.Serializer):
    title = serializers.CharField(help_text="곡 제목")
    category = serializers.CharField(help_text="곡 범주")
    star_rating = serializers.CharField(help_text="1~3 이내 지정 가능. 숫자가 클수록 갓곡")