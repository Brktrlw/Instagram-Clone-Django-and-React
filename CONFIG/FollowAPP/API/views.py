from rest_framework.generics import CreateAPIView,DestroyAPIView
from .serializers import SerializerFollow,SerializerCreateRequest
from UserAPP.models import ModelFollower,ModelUser
from django.shortcuts import get_object_or_404
from NotificationAPP.models import ModelNotification,ModelRequest


class UnfollowerUserAPIView(DestroyAPIView):
    #Takipten çık
    lookup_field     = "follower__username"
    serializer_class = SerializerFollow
    queryset         = ModelFollower.objects.all()

    def get_object(self):
        follower = get_object_or_404(ModelUser,username=self.kwargs.get("follower__username"))
        following=self.request.user
        return get_object_or_404(ModelFollower,follower=follower,following=following)

    def perform_destroy(self, instance):
        ModelNotification.objects.filter(receiver_user=instance.follower,sender_user=self.request.user,post=None).delete()
        instance.delete()

class FollowUserAPIView(CreateAPIView):
    # Herkese açık hesabı takip et
    serializer_class  = SerializerFollow
    queryset          = ModelFollower.objects.all()

    def perform_create(self, serializer):
        # Takip ederken karşı tarafa bildirim de gönderiyoruz
        receiver_user = get_object_or_404(ModelUser,username=serializer.validated_data["follower"].get("username"))
        sender_user   = self.request.user
        ModelNotification.objects.create(receiver_user=receiver_user,sender_user=sender_user,notificationType=2)
        serializer.save(follower=receiver_user,following=sender_user) # Takipçilere ekler

class CreateRequestFollowAPIView(CreateAPIView):
    # gizli hesaba istek atma
    serializer_class =  SerializerCreateRequest
    queryset         =  ModelRequest.objects.all()

    def perform_create(self, serializer):
        receiver_user = get_object_or_404(ModelUser,username=serializer.validated_data["receiver_user"].get("username"))
        sender_user   = self.request.user
        ModelNotification.objects.create(receiver_user=receiver_user, sender_user=sender_user, notificationType=3)

        serializer.save(receiver_user=receiver_user, sender_user=sender_user)  # Takipçilere ekler








