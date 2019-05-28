import math
from django.db import models
from django.utils.text import Truncator
from django.contrib.auth.models import User as 회원
from django.utils.html import mark_safe
from markdown import markdown


class 그리드헤드텝(models.Model):
    헤더 = models.CharField(max_length=30)
    그리드 = models.CharField(max_length=30)
    순서 = models.IntegerField(null=True)

    def __str__(self):
        return self.헤더


class 게시판텝(models.Model):
    이름 = models.CharField(max_length=30)
    설명 = models.CharField(max_length=100)

    def __str__(self):
        return self.이름

    def 게시된글수(self):
        return 글텝.objects.filter(주제__게시판=self).count()

    def 최근작성글(self):
        return 글텝.objects.filter(주제__게시판=self).order_by('-작성일').first()


class 주제텝(models.Model):
    주제 = models.CharField(max_length=255)
    게시일 = models.DateTimeField(auto_now_add=True)
    게시판 = models.ForeignKey(게시판텝, related_name='주제들', on_delete=models.CASCADE)
    게시자 = models.ForeignKey(회원, related_name='주제들', on_delete=models.CASCADE)
    조회수 = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.주제

    def get_page_count(self):
        count = self.글들.count()
        pages = count / 3
        return math.ceil(pages)

    def has_many_pages(self, count=None):
        if count is None:
            count = self.get_page_count()
        return count > 3

    def get_page_range(self):
        count = self.get_page_count()
        if self.has_many_pages(count):
            return range(1, 5)
        return range(1, count + 1)

    def get_last_ten_posts(self):
        return self.글들.order_by('-작성일')[:10]


class 글텝(models.Model):
    글 = models.TextField(max_length=4000)
    주제 = models.ForeignKey(주제텝, related_name='글들', on_delete=models.CASCADE)
    작성자 = models.ForeignKey(회원, related_name='글들', on_delete=models.CASCADE)
    작성일 = models.DateTimeField(auto_now_add=True)
    수정자 = models.ForeignKey(회원, null=True, related_name='+', on_delete=models.CASCADE)
    수정일 = models.DateTimeField(null=True)

    def __str__(self):
        머릿말 = Truncator(self.글)
        return 머릿말.chars(30)

    def get_message_as_markdown(self):
        return mark_safe(markdown(self.글, safe_mode='escape'))


class 게시판그리드헤드텝(models.Model):
    순서 = models.IntegerField(null=True)
    헤더 = models.CharField(max_length=10)

    def __str__(self):
        return self.헤더


class 주제그리드헤드텝(models.Model):
    순서 = models.IntegerField(null=True)
    헤더 = models.CharField(max_length=10)

    def __str__(self):
        return self.헤더


