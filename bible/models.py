from django.db import models
from django.contrib.auth.models import User


class 성경책텝(models.Model):

    책목록 = (
        (1, '개역개정 성경전서'),
        (2, 'NIV Bible'),
        (3, 'Good News Bible'),
    )


    언어목록 = (
        (1, '한국어'),
        (2, 'English'),
    )

    서명 = models.PositiveIntegerField(choices=책목록)
    언어 = models.PositiveIntegerField(choices=언어목록)


    def __str__(self):
        return self.get_서명_display()


class 성경권텝(models.Model):
    구분목록 = (
        (1, '구약'),
        (2, '신약'),
        (3, 'Old Testment'),
        (4, 'New Testment'),
    )

    권목록 = (
        ('한국어', (
            ('창', '창세기'),
            ('출', '출애굽기'),
        )),
        ('English', (
            ('Gen', 'Genesis'),
            ('Exo', 'Exodus'),
        )),
    )


    권명 = models.CharField(max_length=6, choices=권목록)
    구분 = models.PositiveIntegerField(choices=구분목록)
    순서 = models.PositiveIntegerField()
    절수 = models.PositiveIntegerField()
    서명 = models.ForeignKey(성경책텝, related_name='권들', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.get_권명_display()


class 성경장텝(models.Model):
    번호 = models.PositiveIntegerField()
    권 = models.ForeignKey(성경권텝, related_name='장들', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.번호)


class 성경절텝(models.Model):
    번호 = models.PositiveIntegerField()
    내용 = models.TextField()
    단락시작 = models.BooleanField(default=False)
    장 = models.ForeignKey(성경장텝, related_name='절들', blank=True, null=True, on_delete=models.SET_NULL)
    작성자 = models.ForeignKey(User, related_name='작성자', blank=True, null=True, on_delete=models.SET_NULL)
    작성일 = models.DateTimeField(auto_now_add=True)
    수정일 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        result = "{:_<4}{}".format(str(self.번호), self.내용)
        return result

    # def save(self, request):
    #     작성자 = request.User


class 성경글텝(models.Model):
    제목 = models.CharField(max_length=100)
    권 = models.ForeignKey(성경권텝, related_name='글들', blank=True, null=True, on_delete=models.SET_NULL)
    시작장 = models.PositiveIntegerField()
    시작절 = models.PositiveIntegerField()
    종료장 = models.PositiveIntegerField()
    종료절 = models.PositiveIntegerField()

    def __str__(self):
        return self.제목