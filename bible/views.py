from django.shortcuts import render

from .models import 성경책텝
from .models import 성경권텝
from .models import 성경장텝
from .models import 성경절텝
from .models import 성경글텝

def 성경구절뷰(request):
    구절 = 성경절텝.objects.filter(번호__range=(1,6)).order_by('번호')

    return render(request, 'bible/성경구절.html', {'구절':구절})