from rest_framework import serializers
from api.models import Article

# Implementation of Serializer

class ArticleSerializer(serializers.Serializer):
    title             = serializers.CharField(max_length=128)
    author            = serializers.CharField(max_length=64)
    email             = serializers.EmailField(max_length=64)
    created_at        = serializers.DateTimeField()

    def create(self, validated_data):
        """
            Create and return an Article instance, with given validated_data.
        """
        return Article.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        """
        Update and return an Article instance, with given validated_data.
        """
        instance.title          = validated_data.get('title', instance.title)
        instance.author         = validated_data.get('author', instance.author)
        instance.email          = validated_data.get('email', instance.email)
        instance.created_at     = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance
