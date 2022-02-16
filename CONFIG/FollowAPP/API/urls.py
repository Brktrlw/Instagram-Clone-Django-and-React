
from django.urls import path
from .views import FollowUserAPIView,UnfollowerUserAPIView,CreateRequestFollowAPIView,UnRequestFollowAPIView,AllFollowProccessAPIView

app_name="follow"
urlpatterns = [
    path('follow/', FollowUserAPIView.as_view(), name="url_follow"),                               #  Kullanıcıyı takip etme   (anında takip)
    path("unfollow/<follower__username>",UnfollowerUserAPIView.as_view(),name="url_follower"),     #  Kullanıcıyı unfollow etme

    path("request/",CreateRequestFollowAPIView.as_view(),name="url_request"),                      # Gizli kullanıcıya istek atma
    path("unrequest/<follower__username>",UnRequestFollowAPIView.as_view(),name="url_following") ,  # İsteği geri çekme

    path("follow-user/",AllFollowProccessAPIView.as_view())    # takip etme,takibi geri çekme,istek atma ve isteği geri çekme ( bildirimler ile)
]

