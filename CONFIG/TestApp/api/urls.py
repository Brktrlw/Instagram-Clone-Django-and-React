
from django.urls import path
from .views import ListTestAPIView,PostDeleteAPIView


urlpatterns = [
    path("list/",ListTestAPIView.as_view()),
    path("delete/<pk>", PostDeleteAPIView.as_view()),
]


