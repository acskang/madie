from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import 게시판텝, 게시판테이블헤드


def 게시판(request):
    결과 = dict()
    게시판들 = 게시판텝.objects.all()
    헤더 = 게시판테이블헤드.objects.all()

    결과['헤더'] = 헤더
    결과['게시판들'] = 게시판들

    return render( request, '게시판.html', {'뷰결과': 결과} )


def 게시판_주제(request, id):

    게시판 = get_object_or_404(게시판텝, pk=id)

    return render(request, '주제.html', {'뷰결과':게시판})