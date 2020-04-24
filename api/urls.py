from django.urls import path
from api.views import (
    function_based_views_article_list,
    function_based_views_article_single,
    function_based_api_views_article_list,
    function_based_api_views_article_single
)

app_name = 'api'

urlpatterns = [
    # Function based article list view
    # path('', function_based_views_article_list, name='articles'),

    # Function based article single view
    # path('<int:pk>/', function_based_views_article_single, name= 'article_single'),

    # Function based api article list view
    path('', function_based_api_views_article_list, name='articles'),
    
    # Function based api article single view
    path('<int:pk>/', function_based_api_views_article_single, name= 'article_single')
]
