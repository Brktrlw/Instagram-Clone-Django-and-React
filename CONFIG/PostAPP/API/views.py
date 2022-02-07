from rest_framework.generics import CreateAPIView,DestroyAPIView
from PostAPP.models import ModelPost
from .serializers import SerializerPostCreateDelete
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
class PostCreateAPIView(CreateAPIView):
    queryset         = ModelPost.objects.all()
    serializer_class = SerializerPostCreateDelete

    def perform_create(self, serializer):       # Post kayıt edilirken kullanıcıyı giriş yapmış kullanıcı olarak ayarlıyoruz
        serializer.save(user=self.request.user)

class DeletePostAPIView(DestroyAPIView):
    queryset           = ModelPost.objects.all()
    serializer_class   = SerializerPostCreateDelete
    lookup_field       = "unique_id"
    permission_classes = [IsAuthenticated,IsOwner]