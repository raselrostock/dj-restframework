from django.urls import path
from api.views import (
    function_based_views_article_list,
    function_based_views_article_single
)

app_name = 'api'

urlpatterns = [
    path('', function_based_views_article_list, name='articles'),
    path('<int:pk>/', function_based_views_article_single, name= 'article_single')
]
