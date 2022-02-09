from rest_framework import serializers
from UserAPP.models import ModelFollower

class SerializerFollow(serializers.ModelSerializer):
    class Meta:
        model  = ModelFollower
        fields = ("follower",)

