from django.contrib import admin

from . import models

admin.site.register(models.게시판그리드헤드텝)
admin.site.register(models.주제그리드헤드텝)

admin.site.register(models.게시판텝)
admin.site.register(models.주제텝)
admin.site.register(models.글텝)