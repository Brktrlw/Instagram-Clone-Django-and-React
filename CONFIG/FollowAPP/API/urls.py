
from django.urls import path
from .views import FollowUserAPIView,UnfollowerUserAPIView,CreateRequestFollowAPIView,UnRequestFollowAPIView

app_name="follow"
urlpatterns = [
    path('follow/', FollowUserAPIView.as_view(), name="url_follow"),        #  Kullanıcıyı takip etme    (anında takip)
    path("unfollow/<follower__username>",UnfollowerUserAPIView.as_view()),  #  Kullanıcıyı unfollow etme

    path("request/",CreateRequestFollowAPIView.as_view()),                  # Gizli kullanıcıya istek atma
    path("unrequest/<follower__username>",UnRequestFollowAPIView.as_view())                     # İsteği geri çekme
]

