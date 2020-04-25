from django.shortcuts import render
from django.http import Http404

# Thirdparty imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# App imports
from api.model_serializers import ArticleModelSerializer
from api.models import Article

class Class_Based_API_Article_Single(APIView):
    '''
    Show a article detail, edit the article, delete the article
    '''
    def get_article(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get( self, request, pk, format=None ):
        article = self.get_article(pk)
        serializer = ArticleModelSerializer(article)
        return Response(serializer.data)

    def put( self, request, pk, format=None):
        article = self.get_article(pk)
        serializer= ArticleModelSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete( self, request, pk, format=None ):
        article = self.get_article(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
