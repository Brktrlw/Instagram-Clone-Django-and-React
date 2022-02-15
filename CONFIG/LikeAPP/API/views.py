from rest_framework.generics import ListAPIView,CreateAPIView
from LikeAPP.models import ModelPostLike,ModelCommentLike
from .serializers import SerializerPostLikesList,SerializerCommentLikesList,SerializerPostLike,SerializerCommentLike
from rest_framework.permissions import IsAuthenticated
from .permissions import IsFollowingOrOwnPost,IsFollowingOrOwnComment
from PostAPP.models import ModelPost
from django.shortcuts import get_object_or_404
from CommentAPP.models import ModelComment


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

class PostLikeCreateDeleteAPIView(CreateAPIView):
    # Postu beğenmeye yarar,eğer beğeni varsa beğeniyi GERİ ÇEKMEYİ sağlayan view ( Bu kontrol model içerisinde SIGNAL ile yapılıyor)
    serializer_class   = SerializerPostLike
    queryset           = ModelPostLike.objects.all()
    permission_classes = [IsAuthenticated,IsFollowingOrOwnPost]

    def perform_create(self, serializer):
        post = get_object_or_404(ModelPost,unique_id=self.kwargs.get("unique_id"))
        serializer.save(user=self.request.user,post=post)

class CommentLikeCreateDeleteAPIView(CreateAPIView):
    # Yorumu beğenmeye yarar,eğer beğeni varsa beğeniyi GERİ ÇEKMEYİ sağlayan view ( Bu kontrol model içerisinde SIGNAL ile yapılıyor)
    serializer_class   = SerializerCommentLike
    queryset           = ModelCommentLike.objects.all()
    permission_classes = [IsAuthenticated,IsFollowingOrOwnComment]
    def perform_create(self, serializer):
        comment = get_object_or_404(ModelComment,unique_id=self.kwargs.get("unique_id"))
        serializer.save(user=self.request.user,comment=comment)