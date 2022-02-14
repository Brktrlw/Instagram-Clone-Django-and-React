from django.urls import path
from .views import UserCurrentStoriesListAPIView,HomePageStoriesListAPIView


app_name="stories"
urlpatterns = [
    path('<str:user__username>/',UserCurrentStoriesListAPIView.as_view()),
    path('all/a/', HomePageStoriesListAPIView.as_view()),
]


