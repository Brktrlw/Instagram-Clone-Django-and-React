from rest_framework.generics import CreateAPIView,DestroyAPIView
from .serializers import SerializerFollow,SerializerCreateRequest,SerializerDENEME
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

class UnRequestFollowAPIView(DestroyAPIView):
    # Takip isteğini sil
    lookup_field     = "follower__username"
    serializer_class = SerializerCreateRequest
    queryset         = ModelRequest.objects.all()

    def get_object(self):
        follower  = get_object_or_404(ModelUser,username=self.kwargs.get("follower__username"))
        following = self.request.user
        return get_object_or_404(ModelRequest,receiver_user=follower,sender_user=following)

    def perform_destroy(self, instance):
        ModelNotification.objects.filter(receiver_user=instance.receiver_user,sender_user=self.request.user,post=None).delete()
        instance.delete()

class DENEME_API(CreateAPIView):
    serializer_class = SerializerDENEME
    queryset = ModelFollower.objects.all()

    def perform_create(self, serializer):
        senderUser   = self.request.user
        receiverUser = get_object_or_404(ModelUser,username=serializer["receiver"].value)
        followOBJ    = ModelFollower.objects.filter(follower=receiverUser,following=senderUser)
        if followOBJ.exists():
            #takibi bırakma
            followOBJ.delete()
            ModelNotification.objects.filter(receiver_user=receiverUser, sender_user=senderUser, notificationType="2").delete()
        else:
            #takip etme
            if receiverUser.private:
                #hesap gizliyse
                requestOBJ=ModelRequest.objects.filter(receiver_user=receiverUser,sender_user=senderUser)
                if requestOBJ:
                    #istek zaten atmış ,isteği geri çekiyoruz
                    requestOBJ.delete()
                    ModelNotification.objects.filter(receiver_user=receiverUser,sender_user=senderUser,notificationType="3").delete()
                else:
                    #istek atmamış istek oluşturuyoruz
                    ModelRequest.objects.create(receiver_user=receiverUser, sender_user=senderUser)
                    ModelNotification.objects.create(receiver_user=receiverUser,sender_user=senderUser,notificationType="3")
            else:
                #gizli hesap değilse direkt takip ediyoruz
                ModelFollower.objects.create(follower=receiverUser,following=senderUser)
                ModelNotification.objects.create(receiver_user=receiverUser,sender_user=senderUser,notificationType="2")


