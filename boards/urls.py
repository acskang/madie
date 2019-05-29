from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from boards import views
from accounts import views as accounts_views

urlpatterns = [
    path('', views.게시판목록뷰.as_view(), name='게시판목록'),
    path('<id>/', views.주제목록뷰.as_view(), name='주제목록'),
    path('<게시판_id>/새글/', views.새글, name='새글'),
    path('<id>/주제/<주제_id>/', views.댓글목록뷰.as_view(), name='댓글목록'),
    path('<게시판_id>/주제/<주제_id>/댓글/', views.댓글, name='댓글'),
    path('<게시판_id>/주제/<주제_id>/글/<글_pk>/수정/',
        views.글수정뷰.as_view(), name='댓글수정'),
]