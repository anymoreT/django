from rest_framework import  serializers
from .models import Poem
from .models import MyModel

class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = ["author", "type", "title", "date"]


class PoemNormalSerializer(serializers.Serializer):
    author = serializers.CharField(read_only=True)
    type = serializers.CharField(required=True, allow_blank=True, max_length=100)
    def create(self, validated_data):
        """
        """
        return Poem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('author', instance.author)
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance



class MyModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyModel
        fields = ('id', 'file', 'created_at')