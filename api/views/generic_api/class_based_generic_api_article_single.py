from django.shortcuts import render
from django.http import Http404

# Thirdparty imports
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

# App imports
from api.model_serializers import ArticleModelSerializer
from api.models import Article

class Class_Based_Generic_Api_Article_Single(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer