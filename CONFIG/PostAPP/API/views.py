from rest_framework.generics import CreateAPIView,DestroyAPIView,ListAPIView
from PostAPP.models import ModelPost
from .serializers import SerializerPostCreateDelete,SerializerOwnPostList,SerializerFollowersPostList
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from UserAPP.models import ModelUser,ModelFollower

class PostCreateAPIView(CreateAPIView):
    queryset         = ModelPost.objects.all()
    serializer_class = SerializerPostCreateDelete

    def perform_create(self, serializer):       # Post kayıt edilirken kullanıcıyı giriş yapmış kullanıcı olarak ayarlıyoruz
        user = ModelUser.objects.filter(username="admin")
        serializer.save(user=user)

class DeletePostAPIView(DestroyAPIView):
    queryset           = ModelPost.objects.all()
    serializer_class   = SerializerPostCreateDelete
    lookup_field       = "unique_id"
    permission_classes = [IsAuthenticated,IsOwner]

class OwnPostListAPIView(ListAPIView):
    serializer_class   = SerializerOwnPostList
    permission_classes = [IsAuthenticated]
    #pagination_class = []
    def get_queryset(self):
        return ModelPost.objects.filter(user=self.request.user)

class FollowersPostListAPIView(ListAPIView):
    serializer_class = SerializerFollowersPostList
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        myFollowings = self.request.user.followings.all().values_list('follower_id')
        posts        = ModelPost.objects.filter(user_id__in=myFollowings).order_by("-createdDate")
        return posts

