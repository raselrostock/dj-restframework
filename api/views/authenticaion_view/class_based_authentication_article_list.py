from django.shortcuts import render

# Thirdparty imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# App imports
from api.model_serializers import ArticleModelSerializer
from api.models import Article

# Generic API VIEW
# class Class_Based_Authentication_Article_List(ListModelMixin, CreateModelMixin, GenericAPIView):
#     '''
#     List all articles, or create a new article
#     '''
#     authentication_classes= [ SessionAuthentication, BasicAuthentication ]
#     permission_classes=[ IsAuthenticated]
#     queryset = Article.objects.all()
#     serializer_class = ArticleModelSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# API VIEW
class Class_Based_Authentication_Article_List(APIView):
    '''
    List all articles, or create a new article
    '''
    authentication_classes= [ SessionAuthentication, BasicAuthentication ]
    permission_classes=[ IsAuthenticated]
    # queryset = Article.objects.all()
    # serializer_class = ArticleModelSerializer

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