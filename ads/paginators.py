from rest_framework.pagination import PageNumberPagination


class AdPaginator(PageNumberPagination):
    """
    Пагинация:
    page_size - количество элементов на странице
    page_size_query_param - параметр запроса для указания количества элементов на странице
    """
    page_size = 4
    page_size_query_param = "page_size"
