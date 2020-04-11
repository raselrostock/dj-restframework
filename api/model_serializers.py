from rest_framework import serializers

from api.models import Article

class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [ 'title', 'author', 'email', 'created_at' ]