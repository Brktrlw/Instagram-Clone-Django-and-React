from rest_framework import serializers
from PostAPP.models import ModelPost

class SerializerPostCreate(serializers.ModelSerializer):
    class Meta:
        model  = ModelPost
        fields = ("title","images")






