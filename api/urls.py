from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
  성경책뷰, 성경권뷰, 성경장뷰, 성경절뷰, 성경글뷰)

from .views import ArticleViewSet

schema_view = get_swagger_view(title='ahading API')

router = routers.DefaultRouter()
router.register('article', ArticleViewSet)
router.register('성경책', 성경책뷰)
router.register('성경권', 성경권뷰)
router.register('성경장', 성경장뷰)
router.register('성경절', 성경절뷰)
router.register('성경글', 성경글뷰)


urlpatterns = [
    path('', include(router.urls)),
    path('doc/', schema_view, name='연동방법'),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]