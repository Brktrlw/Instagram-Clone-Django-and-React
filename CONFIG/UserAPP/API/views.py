from rest_framework.generics import ListAPIView,CreateAPIView
from UserAPP.models import ModelUser
from .serializers import SerializerUserFollowers,SerializerUserFollowings,SerializerUserProfile,SerializerUserRegister,SerializerLoginUserInfo,SerializerUserProfileInfo
from rest_framework.permissions import IsAuthenticated
from PostAPP.API.permissions import IsFollowing
from UserAPP.models import ModelFollower

class WhenLoginUserAPIView(ListAPIView):
    # Giriş yaparken kullanıcı adı ve profil fotoğrafını gönderdiğimiz view
    serializer_class   = SerializerLoginUserInfo
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        #return ModelUser.objects.filter(username=self.request.user.username)
        return ModelUser.objects.filter(username=self.request.user.username)

class UserFollowersAPIView(ListAPIView):
    # kullanıcının adına göre takipçilerini döndürür
    serializer_class   = SerializerUserFollowers
    permission_classes = [IsAuthenticated,IsFollowing]
    def get_queryset(self):
        return self.request.user.followers.all()

class UserFollowingAPIView(ListAPIView):
    # kullanıcının adına göre takip ettiklerini döndürür
    serializer_class   = SerializerUserFollowings
    permission_classes = [IsAuthenticated, IsFollowing]

    def get_queryset(self):
        return self.request.user.followings.all()

class UserProfileAPIView(ListAPIView):
    # Kullanıcının profil bilgilerini gönderdiğimiz serializer
    serializer_class   = SerializerUserProfile
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return ModelUser.objects.filter(username=self.kwargs.get("user__username"))

class UserRegisterAPIView(CreateAPIView):
    # Kullanıcı kayıt işlemi
    serializer_class = SerializerUserRegister
    queryset = ModelUser.objects.all()
    def perform_create(self, serializer):
        serializer.save(private=True)

class UserProfileInfoAPIView(ListAPIView):
    """
     herhangi bir kullanıcının kullanıcı adına göre
     username,pp,isAnyStory,biography,private,followingCount,followerCount bilgilerini verir
    """

    serializer_class = SerializerUserProfileInfo
    def list(self, request, *args, **kwargs):
        # eğer kullanıcının profili gizliye ve takip etmiyorsak isAnyStory daima False olarak döner
        response = super().list(request, args, kwargs)
        userOBJ=ModelUser.objects.get(username=self.kwargs.get("username"))
        isFollowing=ModelFollower.objects.filter(follower=userOBJ,following=request.user).exists()
        if isFollowing==False and userOBJ.private==True:
            response.data[0]["isAnyStory"]=False
        return response
    def get_queryset(self):
        return ModelUser.objects.filter(username=self.kwargs.get("username"))
