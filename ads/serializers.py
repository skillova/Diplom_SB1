from rest_framework import serializers
from .models import Ad, Comment


class AdSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор для модели объявления
    """

    class Meta:
        model = Ad
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор для модели отзыва
    """

    class Meta:
        model = Comment
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для детального просмотра одного объявления
    """

    class Meta:
        model = Ad
        fields = '__all__'
