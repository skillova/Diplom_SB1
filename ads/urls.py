from django.urls import path
from rest_framework.routers import SimpleRouter

from ads.apps import AdsConfig
from ads.views import AdCreateAPIView, AdListAPIView, AdRetrieveAPIView, AdUpdateAPIView, AdDestroyAPIView, \
    MyAdListAPIView, CommentViewSet

app_name = AdsConfig.name

router = SimpleRouter()
router.register(r'(?P<ad_pk>\d+)/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', AdListAPIView.as_view(), name='ad-list'),
    path('ad_create/', AdCreateAPIView.as_view(), name='ad-create'),
    path('mylist/', MyAdListAPIView.as_view(), name='ad-mylist'),
    path('<int:pk>/', AdRetrieveAPIView.as_view(), name='ad-detail'),
    path('<int:pk>/update/', AdUpdateAPIView.as_view(), name='ad-update'),
    path('<int:pk>/delete/', AdDestroyAPIView.as_view(), name='ad-delete'),
] + router.urls
