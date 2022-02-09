

from django.urls import path
from .views import PostLikesListAPIView,CommentLikesListAPIView


app_name="likes"
urlpatterns = [
    path('post/list/<unique_id>', PostLikesListAPIView.as_view()),        # 127.0.0.1:8000/api/like/post/list/<>
    path('comment/list/<unique_id>', CommentLikesListAPIView.as_view()),  # 127.0.0.1:8000/api/like/comment/list/<>
]

