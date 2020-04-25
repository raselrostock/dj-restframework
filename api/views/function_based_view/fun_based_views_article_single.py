from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Thirdparty imports
from rest_framework.parsers import JSONParser
from rest_framework import status

# App imports
from api.serializers import ArticleSerializer
from api.models import Article

@csrf_exempt
def function_based_views_article_single(request, pk):
    '''
    Article display, update, delete
    '''
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
