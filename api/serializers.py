from rest_framework import serializers

from bible.models import (
  성경책텝, 성경권텝, 성경장텝, 성경절텝, 성경글텝)

from trot.models import Article


class 성경책시리얼화(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = 성경책텝
    fields = ('id', 'url', '서명', '언어')


class 성경권시리얼화(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = 성경권텝
    fields = ('id', 'url', '권명', '구분', '순서', '절수', '서명')


class 성경장시리얼화(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = 성경장텝
    fields = ('id', 'url', '번호', '권')


class 성경절시리얼화(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = 성경절텝
    fields = ('id', 'url', '번호', '내용', '단락시작', '장', '작성일', '수정일')


class 성경글시리얼화(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = 성경글텝
    fields = ('id', 'url', '제목', '권', '시작장', '시작절', '종료장', '종료절')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'