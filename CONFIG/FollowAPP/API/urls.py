
from django.urls import path
from .views import FollowUserAPIView,UnfollowerUserAPIView

app_name="follow"
urlpatterns = [
    path('follow/<user__username>', FollowUserAPIView.as_view(), name="url_follow"), # Kullanıcıyı takip etme (istek/ya da anında takip)
    path("unfollow/<follower__username>",UnfollowerUserAPIView.as_view())              # Kullanıcıyı unfollow etme

]

