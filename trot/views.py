from django.shortcuts import render, redirect

from .models import 이미지텝
from .forms import 이미지폼


def 이미지뷰(request):
    이미지들 = 이미지텝.objects.all()
    if request.method == 'POST':
        print("한마디", request.POST)
        print("한마디", request.FILES)
        form = 이미지폼(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('이미지목록')
    else:
        form = 이미지폼()
    return render(request, 'trot/이미지목록.html', {'form': form, '이미지들': 이미지들})