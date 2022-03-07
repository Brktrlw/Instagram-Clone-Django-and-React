
from rest_framework import serializers
from TestApp.models import TestModel


class SerializerTest(serializers.ModelSerializer):
    class Meta:
        model=TestModel
        fields="__all__"

class SerializerCreateTest(serializers.ModelSerializer):

    class Meta:
        model=TestModel
        fields="__all__"
