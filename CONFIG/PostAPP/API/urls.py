
from django.urls import path
from .views import PostCreateAPIView,DeletePostAPIView,OwnPostListAPIView,FollowersPostListAPIView

app_name="posts"
urlpatterns = [
    path('create/', PostCreateAPIView.as_view(),name="url_createpost"),
    path('delete/<unique_id>', DeletePostAPIView.as_view(), name="url_deletepost"),
    path("own",OwnPostListAPIView.as_view(),name="url_ownpostlist"),
    path("get", FollowersPostListAPIView.as_view(), name="gett")
]