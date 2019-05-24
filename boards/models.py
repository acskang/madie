from django.db import models
from django.contrib.auth.models import User as 회원


class 게시판텝(models.Model):
    이름 = models.CharField(max_length=30)
    설명 = models.CharField(max_length=100)

    def __str__(self):
        return self.이름


class 주제텝(models.Model):
    주제 = models.CharField(max_length=255)
    발행일 = models.DateTimeField(auto_now_add=True)
    게시판 = models.ForeignKey(게시판텝, related_name='주제들', on_delete=models.CASCADE)
    게시자 = models.ForeignKey(회원, related_name='주제들', on_delete=models.CASCADE)

    def __str__(self):
        return self.주제


class 글텝(models.Model):
    글 = models.TextField(max_length=4000)
    주제 = models.ForeignKey(주제텝, related_name='게시물들', on_delete=models.CASCADE)
    생성일 = models.DateTimeField(auto_now_add=True)
    변경일 = models.DateTimeField(null=True)
    생성자 = models.ForeignKey(회원, related_name='게시물들', on_delete=models.CASCADE)
    변경자 = models.ForeignKey(회원, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return self.글


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