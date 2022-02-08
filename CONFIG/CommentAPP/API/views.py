from rest_framework.generics import ListAPIView
from CommentAPP.models import ModelComment
from .serializers import SerializerCommentListByPost

class CommentListByPostAPIView(ListAPIView): # Herhangibir postun yorumlarını çeker
    serializer_class = SerializerCommentListByPost
    def get_queryset(self):
        return ModelComment.objects.filter(post__unique_id=self.kwargs.get("postunique_id"),parent=None)

