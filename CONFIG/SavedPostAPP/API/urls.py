
from django.urls import path
from .views import SavedUserPostListAPIView


app_name="savedpost"

urlpatterns = [
    path('list/', SavedUserPostListAPIView.as_view(),name="dadfasd"),
]


