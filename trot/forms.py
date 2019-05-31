from PIL import Image
from django import forms
from django.core.files import File
from .models import 이미지텝

class 이미지폼(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    넓이 = forms.FloatField(widget=forms.HiddenInput())
    높이 = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = 이미지텝
        fields = ('파일', 'x', 'y', '넓이', '높이', )

    def save(self):
        사진 = super(이미지폼, self).save()
        print("한마디 = ", dir(사진))

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('넓이')
        h = self.cleaned_data.get('높이')

        원형이미지 = Image.open(사진.file)
        자른이미지 = 원형이미지.crop((x, y, w+x, h+y))
        변형이미지 = 자른이미지.resize((200, 200), Image.ANTIALIAS)
        변형이미지.save(사진.file.path)

        return 변형이미지