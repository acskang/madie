from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from boards import views
from accounts import views as accounts_views


uid_token = r'(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.게시판목록뷰.as_view(), name='게시판목록'),
    path('게시판/<id>/', views.주제목록뷰.as_view(), name='주제목록'),
    path('게시판/<게시판_id>/새글/', views.새글, name='새글'),
    path('게시판/<id>/주제/<주제_id>/', views.댓글목록뷰.as_view(), name='댓글목록'),
    # path('글조회/<id>/주제/<주제_id>/', views.글조회, name='글조회'),
    path('게시판/<게시판_id>/주제/<주제_id>/댓글/', views.댓글, name='댓글'),
    path('게시판/<게시판_id>/주제/<주제_id>/글/<글_pk>/수정/',
        views.글수정뷰.as_view(), name='댓글수정'),
    path('사용자정보수정/', accounts_views.사용자정보수정뷰.as_view(), name='내계정정보'),

    path('가입/', accounts_views.가입, name='가입'),
    path('로그인/', auth_views.LoginView.as_view(template_name='로그인.html'), name='로그인'),
    path('로그아웃/', auth_views.LogoutView.as_view(), name='로그아웃'),
    path('reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'), name='password_reset'),
    path('reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    path('reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    re_path('reset/{}/'.format(uid_token),
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),

    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),
]