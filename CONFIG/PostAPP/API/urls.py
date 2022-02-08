
from django.urls import path
from .views import PostCreateAPIView,DeletePostAPIView,OwnPostListAPIView,FollowersPostListAPIView,UserPostListAPIView,UpdatePostAPIView

app_name="posts"
urlpatterns = [
    path('create/', PostCreateAPIView.as_view(),name="url_createpost"),
    path('delete/<unique_id>', DeletePostAPIView.as_view(), name="url_deletepost"),
    path("own/",OwnPostListAPIView.as_view(),name="url_ownpostlist"),
    path("following-posts", FollowersPostListAPIView.as_view(), name="url_following_post"),
    path("user/<user__username>", UserPostListAPIView.as_view(), name="url_user_post"),
    path("update/<unique_id>", UpdatePostAPIView.as_view(), name="url_updatepost"),
]