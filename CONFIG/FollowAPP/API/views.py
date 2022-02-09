from rest_framework.generics import CreateAPIView,DestroyAPIView
from .serializers import SerializerFollow
from UserAPP.models import ModelFollower,ModelUser
from django.shortcuts import get_object_or_404
from rest_framework import status,viewsets
from rest_framework.response import Response
from django.http import Http404


class UnfollowerUserAPIView(DestroyAPIView):
    lookup_field     = "follower__username"
    serializer_class = SerializerFollow
    queryset         = ModelFollower.objects.all()

    def get_object(self):
        follower = get_object_or_404(ModelUser,username=self.kwargs.get("follower__username"))
        following=self.request.user
        return get_object_or_404(ModelFollower,follower=follower,following=following)

class FollowUserAPIView(CreateAPIView):
    serializer_class  = SerializerFollow
    queryset          = ModelFollower

    def perform_create(self, serializer):
        receiver_user = get_object_or_404(ModelUser,username=self.kwargs.get("user__username"))
        sender_user   = self.request.user
        serializer.save(follower=receiver_user,following=sender_user) # Takipçilere ekler