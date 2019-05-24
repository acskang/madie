from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from .models import 게시판그리드헤드텝
from .models import 주제그리드헤드텝
from .models import 게시판텝, 주제텝, 글텝
from .forms import 새글폼


def 게시판(request):
    결과 = dict()
    게시판들 = 게시판텝.objects.all()
    헤더 = 게시판그리드헤드텝.objects.all()

    결과['헤더'] = 헤더
    결과['게시판들'] = 게시판들

    return render( request, '게시판.html', {'뷰결과': 결과} )


def 주제(request, id):
    결과 = dict()

    헤더 = 주제그리드헤드텝.objects.all()
    게시판 = get_object_or_404(게시판텝, pk=id)
    주제 = 주제텝.objects.filter(게시판=게시판)

    결과['헤더'] = 헤더
    결과['게시판'] = 게시판
    결과['주제'] = 주제

    return render(request, '주제.html', {'뷰결과':결과})


def 새글(request, id):
    게시판 = get_object_or_404(게시판텝, pk=id)
    회원 = User.objects.first()

    if request.method == 'POST':
        새글 = 새글폼(request.POST)
        if 새글.is_valid():
            주제 = 새글.save(commit=False)
            주제.게시판 = 게시판
            주제.게시자 = 회원
            주제.save()
            글 = 글텝.objects.create(
                글=새글.cleaned_data.get('글'),
                주제=주제,
                생성자=회원
                )
        return redirect('주제', id=게시판.pk)
    else:
        폼 = 새글폼()

    return render(request, '새글.html', {'게시판':게시판, '폼':폼})