from rest_framework.generics import ListAPIView
from UserAPP.models import ModelUser
from .serializers import SerializerUserFollowers,SerializerUserFollowings,SerializerUserProfile
from rest_framework.permissions import IsAuthenticated
from PostAPP.API.permissions import IsFollowing


class UserFollowersAPIView(ListAPIView):
    # kullanıcının adına göre takipçilerini döndürür
    serializer_class   = SerializerUserFollowers
    permission_classes = [IsAuthenticated,IsFollowing]
    def get_queryset(self):
        return self.request.user.followers.all()


class UserFollowingAPIView(ListAPIView):
    # kullanıcınına dına göre takip ettiklerini döndürür
    serializer_class   = SerializerUserFollowings
    permission_classes = [IsAuthenticated, IsFollowing]

    def get_queryset(self):
        return self.request.user.followings.all()

class UserProfileAPIView(ListAPIView):
    # Kullanıcının profil bilgilerini gönderdiğimiz serializer
    serializer_class   = SerializerUserProfile

    def get_queryset(self):
        return ModelUser.objects.filter(username=self.kwargs.get("user__username"))
