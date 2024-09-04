from django_filters import rest_framework as filters
from ads.models import Ad


class AdFilter(filters.FilterSet):
    """
    Класс для фильтрации объявлений по названию
    """
    title = filters.CharFilter(field_name="title", lookup_expr="icontains",)

    # CharFilter — специальный фильтр, который позволяет искать совпадения в текстовых полях модели
    # icontains: Нечувствительное к регистру содержание подстроки
    class Meta:
        model = Ad
        fields = ("title",)
