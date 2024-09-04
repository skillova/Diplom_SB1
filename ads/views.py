from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .filters import AdFilter
from .models import Ad, Comment
from .serializers import AdDetailSerializer, CommentSerializer, AdSerializer


class AdCreateAPIView(generics.CreateAPIView):
    """
    Контроллер создания объявлений.
    """
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()


class AdListAPIView(generics.ListAPIView):
    """
    Контроллер для просмотра списка всех объявлений
    """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter


class AdRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер для просмотра объявления
    """
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()


class AdUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер для изменения объявления
    """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()


class AdDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер для удаления объявления
    """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()


class MyAdListAPIView(generics.ListAPIView):
    """
    Контроллер для просмотра списка объявлений пользователя
    """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для модели отзыва
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
