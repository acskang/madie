from django.shortcuts import render
from django.http import HttpResponse

from .models import 게시판텝, 게시판테이블헤드


def 첫장(request):
    결과 = dict()
    판들 = 게시판텝.objects.all()
    헤더 = 게시판테이블헤드.objects.all()

    결과['판들'] = 판들
    결과['헤더'] = 헤더

    return render( request, '첫장.html', {'뷰결과': 결과} )