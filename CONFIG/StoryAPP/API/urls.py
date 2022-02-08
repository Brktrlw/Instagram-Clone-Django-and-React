from django.urls import path
from .views import UserCurrentStoriesListAPIView


app_name="stories"
urlpatterns = [
    path('<str:user__username>/',UserCurrentStoriesListAPIView.as_view()),
]


