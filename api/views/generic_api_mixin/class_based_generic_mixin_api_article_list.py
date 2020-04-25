from django.shortcuts import render
from django.http import Http404

# Thirdparty imports
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response

# App imports
from api.model_serializers import ArticleModelSerializer
from api.models import Article

class Class_Based_Generic_Mixin_API_Article_List(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)