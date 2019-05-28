from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, ListView
from django.utils.decorators import method_decorator
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.urls import reverse

from django.db.models import Count
from django.utils import timezone

from .models import 게시판그리드헤드텝
from .models import 주제그리드헤드텝
from .models import 그리드헤드텝
from .models import 게시판텝, 주제텝, 글텝
from .forms import 새글폼, 댓글폼


class 게시판목록뷰(ListView):
    model = 게시판텝
    context_object_name = '게시판목록'
    template_name = '게시판목록.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        kwargs['헤드'] = self.헤드
        kwargs['게시판'] = self.게시판
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.헤드 = 그리드헤드텝.objects.filter(그리드='게시판').order_by('순서')
        self.게시판 = 게시판텝.objects.all()
        queryset = self.게시판
        return queryset


class 주제목록뷰(ListView):
    model = 게시판텝
    context_object_name = '게시판들'
    template_name = '주제목록.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        kwargs['헤더'] = self.헤더
        kwargs['게시판'] = self.게시판
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.헤더 = 주제그리드헤드텝.objects.all()
        self.게시판 = get_object_or_404(게시판텝, pk=self.kwargs.get('id'))
        queryset = self.게시판.주제들.order_by('-게시일').annotate(댓글수=Count('주제') - 1)

        return queryset


class 댓글목록뷰(ListView):
    model = 글텝
    context_object_name = '글들'
    template_name = '댓글목록.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):

        session_key = 'viewed_topic_{}'.format(self.주제.pk)
        if not self.request.session.get(session_key, False):
            self.주제.조회수 += 1
            self.주제.save()
            self.request.session[session_key] = True

        kwargs['주제'] = self.주제
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.주제 = get_object_or_404(주제텝, 게시판__pk=self.kwargs.get('id'), pk=self.kwargs.get('주제_id'))
        queryset = self.주제.글들.order_by('작성일')
        return queryset


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
        return redirect('댓글목록', 게시판.pk, 주제.pk)
    else:
        폼 = 새글폼()

    return render(request, '새글.html', {'게시판':게시판, 'form':폼})


# def 글조회(request, id, 주제_id):
#     주제 = get_object_or_404(주제텝, 게시판_id=id, pk=주제_id)
#     주제.조회수 += 1
#     주제.save()
#     return render(request, '글조회.html', {
#         '주제':주제
#         })


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

            주제.수정일 = timezone.now()
            주제.save()

            topic_url = reverse('댓글목록', kwargs={'id': 게시판_id, '주제_id': 주제_id})
            topic_post_url = '{url}?page={page}#{id}'.format(
                url=topic_url,
                id=글.pk,
                page=주제.get_page_count()
            )

            return redirect(topic_post_url)
    else:
        댓글 = 댓글폼()

    return render(request, '댓글.html', {'주제':주제, 'form':댓글})


@method_decorator(login_required, name='dispatch')
class 글수정뷰(UpdateView):
    model = 글텝
    fields = ('글',)
    template_name = '글수정.html'
    pk_url_kwarg = '글_pk'
    context_object_name = '글'

    def form_valid(self, form):
        게시물 = form.save(commit=False)
        게시물.수정자 = self.request.user
        게시물.수정일 = timezone.now()
        게시물.save()
        return redirect('댓글목록', id=게시물.주제.게시판.pk, 주제_id=게시물.주제.pk)