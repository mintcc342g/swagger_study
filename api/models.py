from django.db import models

# Create your models here.

class Music(models.Model):
    ONE_STAR = 1
    TWO_STAR = 2
    THREE_STAR = 3
    STARS = (
        (ONE_STAR, '좋음'),
        (TWO_STAR, '매우 좋음'),
        (THREE_STAR, '고귀함'),
    )

    CATEGORY = (
        ('JPOP', '제이팝'),
        ('POP', '팝송'),
        ('CLASSIC', '클래식'),
        ('ETC', '기타등등'),
    )

    id = models.BigAutoField(primary_key=True, verbose_name='music_id')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='추가된 날짜')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='업뎃 된 날짜')
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name='삭제된 날짜')
    singer = models.CharField(null=False, max_length=128, verbose_name='가수명')
    title = models.CharField(null=False, max_length=128, verbose_name='곡명')
    category = models.CharField(blank=True, null=True, max_length=32, choices=CATEGORY, verbose_name='범주')
    star_rating = models.PositiveSmallIntegerField(blank=True, null=True, choices=STARS, default=ONE_STAR, verbose_name='곡 선호도')

    class Meta:
        # abstract = True  # sqlite3 사용 시 어째선지 이게 있으면 마이그레이션이 안 됨.
        managed = True
        db_table = 'musics'
        app_label = 'api'
        ordering = ['star_rating', ]
        verbose_name_plural = '음악'


class PlayList(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name='play_list_id')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='만들어진 날짜')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='업뎃 된 날짜')
    play_list_name = models.CharField(null=False, max_length=128, verbose_name='플레이리스트 이름')
    music = models.ForeignKey(Music, related_name='music', db_column='music_id',
                                    on_delete=models.CASCADE, verbose_name='곡')

    class Meta:
        managed = True
        db_table = 'play_lists'
        app_label = 'api'
        verbose_name_plural = '나의 플레이 리스트'

