import requests, json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, JsonResponse

from .models import 성경책텝
from .models import 성경권텝
from .models import 성경장텝
from .models import 성경절텝
from .models import 성경글텝

from .forms import MyForm

def 성경구절뷰(request):
    구절 = 성경절텝.objects.filter(번호__range=(1,6)).order_by('번호')

    return render(request, 'bible/성경구절.html', {'구절':구절})


textual = dict()
url = "http://34.66.185.123/api/"

def fromajax(request):
  if request.method == "POST":
    textual["text"] = request.POST.get('msgbox', None)
    payload = json.dumps(textual)   # "{\"text\":\"Good Morning\"}"
    headers = {
      'Content-Type': "application/json",
      # 'User-Agent': "PostmanRuntime/7.13.0",
      # 'Accept': "*/*",
      # 'Cache-Control': "no-cache",
      # 'Token': "0f9667ba-34b4-45f3-996e-581a6195e4bf,18dd6da8-6f95-4344-a57b-5e2e7815275c",
      # 'Host': "34.66.185.123",
      # 'accept-encoding': "gzip, deflate",
      # 'content-length': "23",
      # 'Connection': "keep-alive",
      # 'cache-control': "no-cache"
      }
    response = requests.request("POST", url, data=payload, headers=headers)
    text = response.json()['text']

    return JsonResponse({'response': response, 'query': payload})



def sample(request):
  # form = MyForm()
  if request.method == "POST":
    # form = MyForm(request.POST)
    print("세마디: ", request.POST)
    # if form.is_valid():
    # cd = form.cleaned_data
    # print("한마디: ", cd)
    textual["text"] = request.POST.get('msgbox', None)
    payload = json.dumps(textual)   # "{\"text\":\"Good Morning\"}"
    print("두마디: ", payload)
    headers = {
      'Content-Type': "application/json",
      # 'User-Agent': "PostmanRuntime/7.13.0",
      # 'Accept': "*/*",
      # 'Cache-Control': "no-cache",
      # 'Token': "0f9667ba-34b4-45f3-996e-581a6195e4bf,18dd6da8-6f95-4344-a57b-5e2e7815275c",
      # 'Host': "34.66.185.123",
      # 'accept-encoding': "gzip, deflate",
      # 'content-length': "23",
      # 'Connection': "keep-alive",
      # 'cache-control': "no-cache"
      }
    response = requests.request("POST", url, data=payload, headers=headers)
    text = response.json()['text']
    form = MyForm()
    return render(request, 'bible/alpha.html', {'text':text})
  return render(request, 'bible/alpha.html')