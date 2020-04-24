from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Thirdparty imports
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# App imports
from api.serializers import ArticleSerializer
from api.models import Article

@api_view(['GET', 'POST'])
def function_based_api_views_article_list(request):
    '''
    List all articles or create a new article
    '''
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)