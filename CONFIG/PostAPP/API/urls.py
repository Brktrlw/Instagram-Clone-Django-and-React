
from django.urls import path
from .views import PostCreateAPIView,DeletePostAPIView

urlpatterns = [
    path('create/', PostCreateAPIView.as_view(),name="urlcreatepost"),
    path('delete/<unique_id>', DeletePostAPIView.as_view(), name="urldeletepost"),
]