from rest_framework import serializers
from NotificationAPP.models import ModelNotification


class SerializerListNotification(serializers.ModelSerializer):
    sender_username = serializers.CharField(source="sender_user.username")
    post_unique_id  = serializers.CharField(source="post.unique_id")
    post_image      = serializers.ImageField(source="post.images")
    notifType       = serializers.IntegerField(source="notificationType")

    class Meta:
        model   = ModelNotification
        fields  = ("sender_username","notifType","post_unique_id","post_image")






