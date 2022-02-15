from django.urls import path
from .views import PostLikesListAPIView,CommentLikesListAPIView,PostLikeCreateDeleteAPIView,CommentLikeCreateDeleteAPIView


app_name="likes"
urlpatterns = [
    path('post/list/<unique_id>', PostLikesListAPIView.as_view()),
    path('post/create/<unique_id>', PostLikeCreateDeleteAPIView.as_view()),
    path('comment/list/<unique_id>', CommentLikesListAPIView.as_view()),
    path('comment/create/<unique_id>', CommentLikeCreateDeleteAPIView.as_view()),
]

