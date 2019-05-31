from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


class 이미지텝(models.Model):
    파일 = models.ImageField()
    설명 = models.CharField(max_length=255, blank=True)
    시간 = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '이미지'
        verbose_name_plural = '이미지들'

    def __str__(self):
        return self.설명