from rest_framework.pagination import PageNumberPagination

class HomePagePostPagination(PageNumberPagination):
    page_size = 5
