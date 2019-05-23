from django.shortcuts import render
from django.http import HttpResponse

from .models import 게시판텝


def 첫장(request):
    판들 = 게시판텝.objects.all()

    return render( request, '첫장.html', {'결과': 판들} )