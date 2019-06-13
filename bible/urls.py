from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.성경구절뷰, name='성경홈'),
    path('chat1/', TemplateView.as_view(template_name='bible/chat1.html'), name='chat1'),
    path('alpha/', views.sample, name='샘플'),
    path('alpha/bb01', views.fromajax, name='fromajax'),
    # path('sample/', views.sample, name='샘플'),
]