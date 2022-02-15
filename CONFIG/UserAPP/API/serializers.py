from rest_framework import serializers
from UserAPP.models import ModelUser,ModelFollower
from django.contrib.auth.hashers import make_password


class SerializerUserFollowers(serializers.ModelSerializer):
    # kullanıcının adına göre takipçilerini döndürür
    follower = serializers.CharField(source="following.username")

    class Meta:
        model  = ModelFollower
        fields = ("follower",)

class SerializerUserFollowings(serializers.ModelSerializer):
    # kullanıcının adına göre takip ettiklerini döndürür
    following = serializers.CharField(source="follower.username")
    class Meta:
        model  = ModelFollower
        fields = ("following",)

class SerializerUserProfile(serializers.ModelSerializer):
    # Kullanıcının profil bilgilerini gönderdiğimiz serializer
    totalFollowers  = serializers.SerializerMethodField()
    totalFollowings = serializers.SerializerMethodField()
    isAnyStory      = serializers.SerializerMethodField()

    def get_isAnyStory(self,obj):
        return obj.is_any_story()

    def get_totalFollowers(self,obj):
        return obj.followers.count()

    def get_totalFollowings(self,obj):
        return obj.followings.count()

    class Meta:
        model  = ModelUser
        fields = ("username","totalFollowers","totalFollowings","biography","isAnyStory","profilePhoto")


class SerializerUserSimpleInfo(serializers.ModelSerializer):
    # Bazı kullanıcı bilgilerini verir
    isAnyStory = serializers.SerializerMethodField()
    profilePicture=serializers.SerializerMethodField()

    def get_profilePicture(self,obj):

        return str(obj.get_profile_photo_url())

    def get_isAnyStory(self,obj):
        return obj.is_any_story()

    class Meta:
        model  = ModelUser
        fields = ("username","isAnyStory","profilePicture")

class SerializerUserRegister(serializers.ModelSerializer):
    # Kullanıcı kayıt olma işlemi
    class Meta:
        model = ModelUser
        fields=("username","first_name","last_name","password","profilePhoto")

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(SerializerUserRegister, self).create(validated_data)

    def validate_password(self,value):
        if len(value)<8:
            raise serializers.ValidationError("Parola 8 karakterden fazla olmalıdır.")