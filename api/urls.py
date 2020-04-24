from django.urls import path
from api.views import (
    function_based_views_article_list,
    function_based_views_article_single,
    function_based_api_views_article_list,
    function_based_api_views_article_single,
    Class_Based_API_Article_List,
    Class_Based_API_Article_Single
)

app_name = 'api'

urlpatterns = [
    # Function based article list view
    # path('', function_based_views_article_list, name='articles'),

    # Function based article single view
    # path('<int:pk>/', function_based_views_article_single, name= 'article_single'),

    # Function based api article list view
    # path('', function_based_api_views_article_list, name='articles'),

    # Function based api article single view
    # path('<int:pk>/', function_based_api_views_article_single, name= 'article_single')

    # Class based api article list view
    path('', Class_Based_API_Article_List.as_view(), name='articles'),

    # Class based api article single view
    path('<int:pk>/', Class_Based_API_Article_Single.as_view(), name= 'article_single')
]
