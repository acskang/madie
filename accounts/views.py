from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

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


@method_decorator(login_required, name='dispatch')
class 사용자정보수정뷰(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email')
    template_name = '사용자정보수정.html'
    success_url = reverse_lazy('로그인')

    def get_object(self):
        return self.request.user