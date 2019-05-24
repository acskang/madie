from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import 가입폼

def 가입(request):
    if request.method == 'POST':
        폼 = 가입폼(request.POST)
        if 폼.is_valid():
            user = 폼.save()
            auth_login(request, user)
            return redirect('게시판')
    else:
        form = 가입폼()

    return render(request, '가입.html', {'form':form})