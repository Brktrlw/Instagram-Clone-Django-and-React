from rest_framework import serializers
from UserAPP.models import ModelFollower
from NotificationAPP.models import ModelNotification,ModelRequest

class SerializerFollow(serializers.ModelSerializer):
    receiver_user = serializers.CharField(source="follower.username")
    class Meta:
        model  = ModelFollower
        fields = ("receiver_user",)

class SerializerCreateRequest(serializers.ModelSerializer):
    receiver_user = serializers.CharField(source="receiver_user.username")
    class Meta:
        model  = ModelRequest
        fields = ("receiver_user",)





