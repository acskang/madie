from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from .models import 게시판그리드헤드텝
from .models import 주제그리드헤드텝
from .models import 게시판텝, 주제텝, 글텝
from .forms import 새글폼, 댓글폼


def 게시판(request):
    결과 = dict()
    게시판들 = 게시판텝.objects.all()
    헤더 = 게시판그리드헤드텝.objects.all()

    return render( request, '게시판.html', {
        '헤더':헤더, '게시판들':게시판들
        })


def 주제(request, id):
    결과 = dict()

    헤더 = 주제그리드헤드텝.objects.all()
    게시판 = get_object_or_404(게시판텝, pk=id)
    주제들 = 게시판.주제들.order_by('-게시일').annotate(댓글수=Count('글들') - 1)

    return render(request, '주제.html', {
        '헤더':헤더, '게시판':게시판, '주제들':주제들
        })


def 글조회(request, 게시판_id, 주제_id):
    주제 = get_object_or_404(주제텝, 게시판_id=게시판_id, pk=주제_id)
    게시물들 = 주제.글들.all().order_by('-작성일')
    주제.조회수 += 1
    주제.save()
    return render(request, '글조회.html', {
        '주제':주제, '게시물들':게시물들
        })


@login_required
def 새글(request, 게시판_id):
    게시판 = get_object_or_404(게시판텝, pk=게시판_id)

    if request.method == 'POST':
        새글 = 새글폼(request.POST)
        if 새글.is_valid():
            주제 = 새글.save(commit=False)
            주제.게시판 = 게시판
            주제.게시자 = request.user
            주제.save()
            글 = 글텝.objects.create(
                글=새글.cleaned_data.get('글'),
                주제=주제,
                작성자=request.user
                )
        return redirect('글조회', 게시판.pk, 주제.pk)
    else:
        폼 = 새글폼()

    return render(request, '새글.html', {'게시판':게시판, 'form':폼})


@login_required
def 댓글(request, 게시판_id, 주제_id):
    주제 = get_object_or_404(주제텝, 게시판_id=게시판_id, pk=주제_id)
    if request.method == 'POST':
        댓글 = 댓글폼(request.POST)
        if 댓글.is_valid():
            글 = 댓글.save(commit=False)
            글.주제 = 주제
            글.작성자 = request.user
            글.save()
            return redirect('글조회', pk, 주제_pk)
    else:
        댓글 = 댓글폼()

    return render(request, '댓글.html', {'주제':주제, 'form':댓글})
