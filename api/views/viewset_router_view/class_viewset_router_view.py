from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Thirdparty imports
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# App imports
from api.model_serializers import ArticleModelSerializer
from api.models import Article

class Article_List_Viewset(ViewSet):
    def list(self, request):
        articles = Article.objects.all()
        serializer= ArticleModelSerializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArticleModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        print(pk)
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleModelSerializer(article)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # queryset = Article.objects.all()
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleModelSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class Article_Detail_Viewset(ViewSet):

#     def retrieve(self, request, pk=None):
#         print(pk)
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, pk=pk)
#         serializer = ArticleModelSerializer(article)
#         return Response(serializer.data)
