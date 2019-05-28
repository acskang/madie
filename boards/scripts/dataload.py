# dataload.py
# 기동 방법
# 1. django shell 에서 기동하는 방법
#   >>> exec(open('dataload.py', encoding='utf8').read())
# 2. django-extensions 으로 기돟하는 방법
#   >>> python manage.py runscript -v3 dataload --script-args "가수로드"

## 스크립트가 있는 폴더를 자동으로 찾아감

import csv
from boards import models


def 헤더로드():
    with open('boards/scripts/initialdata.csv', 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            p = models.그리드헤드텝(
                헤더=row['헤더'],
                그리드=row['그리드'],
                순서=row['순서']
                )
            p.save()


def run(function_name):
    if function_name == '헤더로드':
        헤더로드()
    else:
        print("errors...........")