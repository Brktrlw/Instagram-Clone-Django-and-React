
from django.urls import path
from .views import PostCreateAPIView

urlpatterns = [
    path('create/', PostCreateAPIView.as_view(),name="urlcreatepost"),
]