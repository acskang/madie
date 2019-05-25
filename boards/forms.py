from django import forms

from .models import 주제텝, 글텝

class 새글폼(forms.ModelForm):
    글 = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows':5, 'placeholder':'이 주제에 대한 새로운 아이디어를 적어주세요.'}),
        max_length=4000,
        help_text='4천자까지 입력가능힙니다.'
        )

    class Meta:
        model = 주제텝
        fields = ['주제', '글']


class 댓글폼(forms.ModelForm):
    class Meta:
        model = 글텝
        fields = ['글',]