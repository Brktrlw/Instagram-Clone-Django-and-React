from rest_framework.generics import ListAPIView
from LikeAPP.models import ModelPostLike,ModelCommentLike
from .serializers import SerializerPostLikesList,SerializerCommentLikesList
from rest_framework.permissions import IsAuthenticated
from .permissions import IsFollowingOrOwnPost,IsFollowingOrOwnComment

class PostLikesListAPIView(ListAPIView):
    # Post ID'sine göre o postu beğenen kullanıcıların nickname'ini döndürür
    serializer_class   = SerializerPostLikesList
    permission_classes = [IsAuthenticated,IsFollowingOrOwnPost]
    def get_queryset(self):
        return ModelPostLike.objects.filter(post__unique_id=self.kwargs.get("unique_id"))

class CommentLikesListAPIView(ListAPIView):
    # Yorum ID'sine göre o yorumu beğenen kullanıcıların nickname'ini döndürür
    serializer_class = SerializerCommentLikesList
    permission_classes = [IsAuthenticated,IsFollowingOrOwnComment]
    def get_queryset(self):
        return ModelCommentLike.objects.filter(comment__unique_id=self.kwargs.get("unique_id"))

