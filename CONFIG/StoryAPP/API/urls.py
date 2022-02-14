from django.urls import path
from .views import UserCurrentStoriesListAPIView,HomePageStoriesListAPIView,OwnStoriesListAPIView,StorySeeingCreateAPIView,UsersBySeeingStoryListAPIView


app_name="stories"
urlpatterns = [
    path('username/<str:user__username>/',UserCurrentStoriesListAPIView.as_view()),
    path('homepage/', HomePageStoriesListAPIView.as_view()),
    path("own/",OwnStoriesListAPIView.as_view()),

    path("read/",StorySeeingCreateAPIView.as_view()),
    path("watchedusers/<unique_id>",UsersBySeeingStoryListAPIView.as_view())
]


