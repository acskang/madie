from django.contrib import admin

# from .models import 게시판텝, 주제텝, 게시물텝, 게시판테이블헤드

from . import models

admin.site.register(models.게시판테이블헤드)

admin.site.register(models.게시판텝)
admin.site.register(models.주제텝)
admin.site.register(models.게시물텝)