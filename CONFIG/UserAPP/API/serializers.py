from rest_framework import serializers
from UserAPP.models import ModelUser,ModelFollower


class SerializerUserFollowers(serializers.ModelSerializer):
    follower = serializers.CharField(source="following.username")
    class Meta:
        model  = ModelFollower
        fields = ("follower",)

class SerializerUserFollowings(serializers.ModelSerializer):
    following = serializers.CharField(source="follower.username")

    totalFollower = serializers.ReadOnlyField()
    class Meta:
        model  = ModelFollower
        fields = ("following","totalFollower")

class SerializerUserProfile(serializers.ModelSerializer):
    totalFollowers  = serializers.SerializerMethodField()
    totalFollowings = serializers.SerializerMethodField()

    def get_totalFollowers(self,obj):
        return obj.followers.count()

    def get_totalFollowings(self,obj):
        return obj.followings.count()

    class Meta:
        model  = ModelUser
        fields = ("username","totalFollowers","totalFollowings","biography")



