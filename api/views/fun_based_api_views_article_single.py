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

@api_view(['GET', 'PUT', 'DELETE'])
def function_based_api_views_article_single(request, pk):
    '''
    Article display, update, delete
    '''
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)