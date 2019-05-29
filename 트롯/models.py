from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

class 장르텝(models.Model):
    장르명 = models.CharField(max_length=30, default='트로트', unique=True)
    장르설명 = models.TextField(max_length=4000)

    def __str__(self):
        return self.장르명


class 노래텝(models.Model):

    노래유형 = (
        ('원곡', '원곡'),
        ('번안곡', '번안곡'),
        ('리메이크곡', '리메이크곡'),
        )

    계절유형 = (
        ('봄', '봄'),
        ('여름', '여름'),
        ('가을', '가을'),
        ('겨율', '겨울'),
        ('환절기', '환절기'),
        )

    곡명 = models.CharField(max_length=200, null=True)
    작사가 = models.CharField(max_length=30, null=True)
    작곡가 = models.CharField(max_length=30, null=True)
    가수 = models.CharField(max_length=30, null=True)
    발표년도 = models.IntegerField(null=True)
    유형 = models.CharField(max_length=20, default='원곡', choices=노래유형)
    원곡 = models.CharField(max_length=200, null=True)
    장르 = models.ForeignKey(장르텝, default='트로트', related_name='노래들', on_delete=models.SET_DEFAULT)
    느낌 = models.CharField(max_length=30, null=True)
    계절 = models.CharField(max_length=10, null=True, choices=계절유형)
    날씨 = models.CharField(max_length=20, null=True)
    내용 = models.CharField(max_length=200, null=True)
    회사 = models.CharField(max_length=50, null=True)
    가사 = models.TextField(max_length=4000, null=True)
        
    def __str__(self):
        return self.곡명


class 가수텝(models.Model):
    예명 = models.CharField(max_length=30, null=True)
    본명 = models.CharField(max_length=30, null=True)
    사진 = ProcessedImageField(
        upload_to='albums',
        processors=[ResizeToFit(300)],
        format='JPEG',
        options={'quality': 90}
        )
    출생년도 = models.IntegerField(default=0)
    고향 = models.CharField(max_length=20, null=True)
    데뷔년도 = models.IntegerField(default=0)
    데뷔곡 = models.CharField(max_length=200, null=True)
    소속사 = models.CharField(max_length=50, null=True)
    장르 = models.ForeignKey(장르텝, default='트로트', related_name='가수들', on_delete=models.SET_DEFAULT)
    활동중 = models.BooleanField(default=True)
    대표곡 = models.CharField(max_length=50, null=True)
    최근곡 = models.CharField(max_length=50, null=True)
    공식사이트 = models.URLField(null=True)
        
    def __str__(self):
        return self.예명


class 음원텝(models.Model):
    음원아이디 = models.URLField(null=True)
    곡명 = models.ForeignKey(노래텝, default='모른이름 노래',
        related_name='음원들', on_delete=models.SET_DEFAULT)
    가수 = models.ForeignKey(가수텝, default='모른가수 노래',
        related_name='음원들', on_delete=models.SET_DEFAULT)
    발행년도 = models.IntegerField(default=0)
    음원유형 = models.CharField(max_length=30)
    무대 = models.CharField(max_length=30)
    섬네일 = ProcessedImageField(
        upload_to='albums',
        processors=[ResizeToFit(300)],
        format='JPEG',
        options={'quality': 90}
        )

    def __str__(self):
        return self.곡명