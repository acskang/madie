from django.views.generic.base import RedirectView
from django.urls import path, re_path
from django.views.generic import TemplateView


from django.contrib import admin

from . import views


urlpatterns = [
    path('', views.gallery, name='갤러리'),
    path('<slug>', views.AlbumDetail.as_view(), name='album'),
    path('favicon.ico', RedirectView.as_view(url='/static/icons/favicon.ico', permanent=True)),
    path('/비디오/', TemplateView.as_view(template_name='gallery/cs_videodetail.html'), name='비디오'),
]