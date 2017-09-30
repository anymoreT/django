from rest_framework import  serializers
from .models import RestApi
from rest_framework.decorators import api_view

class RestApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestApi
        fields = ('apiName', 'contType')


class PostSerializer(serializers.Serializer):
    author = serializers.CharField(read_only=True)
    type = serializers.CharField(required=True, allow_blank=True, max_length=100)