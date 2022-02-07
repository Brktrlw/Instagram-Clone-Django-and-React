from rest_framework.generics import CreateAPIView,DestroyAPIView,ListAPIView
from PostAPP.models import ModelPost
from .serializers import SerializerPostCreateDelete,SerializerOwnPostList
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from UserAPP.models import ModelUser

class PostCreateAPIView(CreateAPIView):
    queryset         = ModelPost.objects.all()
    serializer_class = SerializerPostCreateDelete

    def perform_create(self, serializer):       # Post kayıt edilirken kullanıcıyı giriş yapmış kullanıcı olarak ayarlıyoruz
        user=ModelUser.objects.first()
        serializer.save(user=user)

class DeletePostAPIView(DestroyAPIView):
    queryset           = ModelPost.objects.all()
    serializer_class   = SerializerPostCreateDelete
    lookup_field       = "unique_id"
    permission_classes = [IsAuthenticated,IsOwner]

class OwnPostListAPIView(ListAPIView):
    serializer_class   = SerializerOwnPostList
    #permission_classes = [IsAuthenticated]
    pagination_class = []
    def get_queryset(self):
        #return ModelPost.objects.filter(user=self.request.user)
        return ModelPost.objects.all()