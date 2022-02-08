
from django.urls import path
from .views import PostCreateAPIView,DeletePostAPIView,OwnPostListAPIView,FollowersPostListAPIView,UserPostListAPIView,UpdatePostAPIView

app_name="posts"
urlpatterns = [
    path('create/', PostCreateAPIView.as_view(),name="url_createpost"),                     # Post oluşturma
    path('delete/<unique_id>', DeletePostAPIView.as_view(), name="url_deletepost"),         # Post silme
    path("update/<unique_id>", UpdatePostAPIView.as_view(), name="url_updatepost"),         # Post Güncelleme

    path("own/",OwnPostListAPIView.as_view(),name="url_ownpostlist"),                       # Giriş yapmış kullanıcının postları
    path("following-posts", FollowersPostListAPIView.as_view(), name="url_following_post"), # Ana sayfada takip ettiğimiz kullanıcıların postları
    path("user/<user__username>", UserPostListAPIView.as_view(), name="url_user_post"),     # Username'e göre postlar
]