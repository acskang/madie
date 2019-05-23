from django.db import models
from django.contrib.auth.models import User as 회원


class 게시판텝(models.Model):
    게시판명 = models.CharField(max_length=30)
    게시판설명 = models.CharField(max_length=100)

    def __str__(self):
        return self.게시판명


class 주제텝(models.Model):
    주제 = models.CharField(max_length=255)
    발행일자 = models.DateTimeField(auto_now_add=True)
    게시판 = models.ForeignKey(게시판텝, related_name='주제들', on_delete=models.CASCADE)
    주최자 = models.ForeignKey(회원, related_name='주제들', on_delete=models.CASCADE)


class 게시물텝(models.Model):
    게시글 = models.TextField(max_length=4000)
    주제 = models.ForeignKey(주제텝, related_name='게시물들', on_delete=models.CASCADE)
    생성일 = models.DateTimeField(auto_now_add=True)
    변경일 = models.DateTimeField(null=True)
    생성자 = models.ForeignKey(회원, related_name='게시물들', on_delete=models.CASCADE)
    변경자 = models.ForeignKey(회원, null=True, related_name='+', on_delete=models.CASCADE)

