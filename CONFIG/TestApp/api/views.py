
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView
from TestApp.models import TestModel
from .serializers import SerializerTest,SerializerCreateTest


class ListTestAPIView(ListAPIView):
    serializer_class = SerializerTest
    def get_queryset(self):
        return TestModel.objects.all()

class PostDeleteAPIView(DestroyAPIView):
    serializer_class = SerializerCreateTest
    queryset = TestModel.objects.all()

