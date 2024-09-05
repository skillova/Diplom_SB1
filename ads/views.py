from django.shortcuts import get_object_or_404
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

    def perform_create(self, serializer):
        """
        Отношение объявления к автору
        """
        ad = serializer.save()
        ad.author = self.request.user
        ad.save()


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

    def get_queryset(self):
        """
        Список объявлений автора
        """
        user = self.request.user
        queryset = Ad.objects.filter(author=user)
        return queryset


class CommentViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для модели отзыва
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        """
        Метод привязки отзыва к автору и объявлению
        """
        comment = serializer.save()
        comment.author = self.request.user
        comment.ad = Ad.objects.get(pk=self.kwargs["ad_pk"])
        comment.save()

    def get_queryset(self):
        """
        Метод для получения отзывов объявления
        """
        ad_pk = self.kwargs.get("ad_pk")
        ad = get_object_or_404(Ad, id=ad_pk)
        comment_list = ad.comment_ad.all()
        return comment_list

