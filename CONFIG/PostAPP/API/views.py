from rest_framework.generics import CreateAPIView,DestroyAPIView,ListAPIView,UpdateAPIView
from PostAPP.models import ModelPost
from .serializers import SerializerPostCreateDelete,SerializerOwnPostList,SerializerFollowersPostList,SerializerUserPostList,SerializerPostUpdate
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from UserAPP.models import ModelUser
from django.db.models import Q
from .paginations import HomePagePostPagination



class PostCreateAPIView(CreateAPIView):
    # Post olurşturma view
    queryset         = ModelPost.objects.all()
    serializer_class = SerializerPostCreateDelete

    def perform_create(self, serializer):
        # Post kayıt edilirken kullanıcıyı giriş yapmış kullanıcı olarak ayarlıyoruz
        user = ModelUser.objects.filter(username="admin")
        serializer.save(user=user)

class DeletePostAPIView(DestroyAPIView):
    # Post silme işlemi
    queryset           = ModelPost.objects.all()
    serializer_class   = SerializerPostCreateDelete
    lookup_field       = "unique_id"
    permission_classes = [IsAuthenticated,IsOwner]

class UpdatePostAPIView(UpdateAPIView):
    # Postları güncellerken kullandıgımız view
    lookup_field       = "unique_id"
    serializer_class   =  SerializerPostUpdate
    permission_classes = [IsAuthenticated,IsOwner]
    queryset           = ModelPost.objects.all()

class OwnPostListAPIView(ListAPIView):
    # Giriş yapmış olan kullanıcının postları
    serializer_class   = SerializerOwnPostList
    permission_classes = [IsAuthenticated]
    # pagination_class = []
    def get_queryset(self):
        return ModelPost.objects.filter(user=self.request.user)

class FollowersPostListAPIView(ListAPIView):
    # Ana sayfada sadece takip ettiğimiz kullanıcıların postlarının yayınlandığı view
    serializer_class = SerializerFollowersPostList
    permission_classes = [IsAuthenticated]
    pagination_class = HomePagePostPagination

    def get_queryset(self):
        myFollowings = self.request.user.followings.all().values_list('follower_id')
        posts        = ModelPost.objects.filter(Q(user_id__in=myFollowings)| Q(user=self.request.user)).order_by("createdDate")
        return posts

class UserPostListAPIView(ListAPIView):
    #Herhangi bir kullanıcının profilinin görüntülenmesinde görev alır. KULLANICI ADINA GÖRE
    serializer_class = SerializerUserPostList
    #permission_classes = [IsFollowing]

    def list(self, request, *args, **kwargs):
        response=super().list(request,args,kwargs)
        userOBJ=ModelUser.objects.get(username=self.kwargs.get("user__username"))
        _data={
            "username":userOBJ.username,
            "isAnyStory":userOBJ.is_any_story(),
            "profilePicture":userOBJ.get_profile_photo_url(),

        }
        response.data.insert(0,_data)
        return response

    def get_queryset(self):
        return ModelPost.objects.filter(user__username=self.kwargs.get("user__username"))



