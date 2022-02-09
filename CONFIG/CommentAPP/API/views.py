from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView
from CommentAPP.models import ModelComment
from .serializers import SerializerCommentListByPost,SerializerCreateComment,SerializerDeleteComment
from rest_framework.permissions import IsAuthenticated
from .permissions import IsFollowing,IsOwner
from PostAPP.models import ModelPost
from django.shortcuts import get_object_or_404

class CommentListByPostAPIView(ListAPIView):
    # Herhangi bir postun yorumlarını çeker
    serializer_class   = SerializerCommentListByPost
    permission_classes = [IsAuthenticated,IsFollowing]
    def get_queryset(self):
        return ModelComment.objects.filter(post__unique_id=self.kwargs.get("postunique_id"),parent=None)

class CreateCommentAPIView(CreateAPIView):
    # Yorum yapma işlemi view
    queryset           = ModelComment.objects.all()
    serializer_class   = SerializerCreateComment
    permission_classes = [IsFollowing,IsAuthenticated]

    def perform_create(self, serializer):
        post = get_object_or_404(ModelPost,unique_id=self.kwargs.get("postunique_id"))
        serializer.save(post=post,user=self.request.user)

class DeleteCommentAPIView(DestroyAPIView):
    # Yorum silme view
    queryset           = ModelComment.objects.all()
    lookup_field       = "unique_id"
    permission_classes = [IsAuthenticated,IsOwner]
    serializer_class   = SerializerDeleteComment

    def perform_destroy(self, instance):
        if instance.any_children:          # yorumun childları varsa yorum silinirken onları da siler
            instance.delete_all_children()
        instance.delete()












