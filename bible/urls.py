from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.성경구절뷰, name='성경홈'),
]