
from django.urls import path
from .views import SavedUserPostListAPIView,CreateSavedPostAPIView


app_name="savedpost"

urlpatterns = [
    path('list/', SavedUserPostListAPIView.as_view()),
    path('create/<unique_id>', CreateSavedPostAPIView.as_view()),
]


