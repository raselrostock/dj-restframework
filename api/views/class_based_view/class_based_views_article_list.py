from django.shortcuts import render

# Thirdparty imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# App imports
from api.model_serializers import ArticleModelSerializer
from api.models import Article

class Class_Based_API_Article_List(APIView):
    '''
    List all articles, or create a new article
    '''
    def get( self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleModelSerializer(articles, many=True)
        return Response(serializer.data)

    def post( self, request, format=None ):
        serializer = ArticleModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)