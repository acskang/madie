from django.test import TestCase
from django.urls import resolve, reverse


from .views import 첫장

class 홈테스트(TestCase):
    def test_홈뷰상태코드(self):
        url = reverse('홈')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_홈URL해석(self):
        뷰 = resolve('/')
        self.assertEquals(뷰.func, 첫장)