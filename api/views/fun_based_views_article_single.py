from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Thirdparty imports
from rest_framework.parsers import JSONParser

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
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser.parse(request)
        serializer = ArticleSerializer(article, data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)
