from django.views.generic.base import RedirectView
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from . import views
admin.autodiscover()

urlpatterns = [
    path('', views.gallery, name='갤러리'),
    path('<slug>', views.AlbumDetail.as_view(), name='album'),
    path('favicon.ico', RedirectView.as_view(url='/static/icons/favicon.ico', permanent=True)),
]