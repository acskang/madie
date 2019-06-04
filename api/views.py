from django.shortcuts import render
from rest_framework import viewsets

from bible.models import (
  성경책텝, 성경권텝, 성경장텝, 성경절텝, 성경글텝)
from .serializers import (
  성경책시리얼화, 성경권시리얼화, 성경장시리얼화, 성경절시리얼화, 성경글시리얼화)


class 성경책뷰(viewsets.ModelViewSet):
  queryset = 성경책텝.objects.all()
  serializer_class = 성경책시리얼화


class 성경권뷰(viewsets.ModelViewSet):
  queryset = 성경권텝.objects.all()
  serializer_class = 성경권시리얼화


class 성경장뷰(viewsets.ModelViewSet):
  queryset = 성경장텝.objects.all()
  serializer_class = 성경장시리얼화


class 성경절뷰(viewsets.ModelViewSet):
  queryset = 성경절텝.objects.all()
  serializer_class = 성경절시리얼화


class 성경글뷰(viewsets.ModelViewSet):
  queryset = 성경글텝.objects.all()
  serializer_class = 성경글시리얼화