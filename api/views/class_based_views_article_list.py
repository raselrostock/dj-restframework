from django.shortcuts import render

# Thirdparty imports
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import

# App imports
from api.model_serializers import ArticleModelSerializer
from api.models import Article