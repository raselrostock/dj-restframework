from django.shortcuts import render

# Thirdparty imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# App imports
from api.model_serializers import ArticleModelSerializer
from api.models import Article

# Generic API VIEW
class Class_Based_Authentication_Article_Single(
    RetrieveModelMixin, 
    UpdateModelMixin, 
    DestroyModelMixin, 
    GenericAPIView
    ):
    '''
    List all articles, or create a new article
    '''
    authentication_classes= [ SessionAuthentication, BasicAuthentication ]
    permission_classes=[ IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# API VIEW
# class Class_Based_Authentication_Article_Single(APIView):
#     '''
#     List all articles, or create a new article
#     '''
#     authentication_classes= [ SessionAuthentication, BasicAuthentication ]
#     permission_classes=[ IsAuthenticated]
#     # queryset = Article.objects.all()
#     # serializer_class = ArticleModelSerializer

#     def get_article(self, pk):
#         try:
#             return Article.objects.get(pk=pk)
#         except Article.DoesNotExist:
#             raise Http404

#     def get( self, request, pk, format=None ):
#         article = self.get_article(pk)
#         serializer = ArticleModelSerializer(article)
#         return Response(serializer.data)

#     def put( self, request, pk, format=None):
#         article = self.get_article(pk)
#         serializer= ArticleModelSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete( self, request, pk, format=None ):
#         article = self.get_article(pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)