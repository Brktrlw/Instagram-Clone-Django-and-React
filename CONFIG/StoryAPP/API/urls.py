from django.urls import path
from .views import UserStoriesListAPIView


app_name="stories"
urlpatterns = [
    path('<str:user__username>/',UserStoriesListAPIView.as_view()),
]


