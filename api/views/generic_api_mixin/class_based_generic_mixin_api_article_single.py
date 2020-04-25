from django.shortcuts import render
from django.http import Http404

# Thirdparty imports
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response

# App imports
from api.model_serializers import ArticleModelSerializer
from api.models import Article

class Class_Based_Generic_Mixin_API_Article_Single(
    RetrieveModelMixin, 
    UpdateModelMixin, 
    DestroyModelMixin, 
    GenericAPIView
    ):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)