from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Ad
from .serializers import AdDetailSerializer


class AdCreateAPIView(generics.CreateAPIView):
    """
    Контроллер создания объявлений.
    """
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Метод для автоматической привязки объявления к создателю.
        """
        serializer.save(author=self.request.user)
