from django.urls import path, include
from api.views import (
    # function_based_views_article_list,
    # function_based_views_article_single,
    # function_based_api_views_article_list,
    # function_based_api_views_article_single,
    # Class_Based_API_Article_List,
    # Class_Based_API_Article_Single,
    # Class_Based_Generic_Api_Article_list,
    # Class_Based_Generic_Api_Article_Single,
    # Class_Based_Generic_Mixin_API_Article_List,
    # Class_Based_Generic_Mixin_API_Article_Single,
    # Class_Based_Authentication_Article_List,
    # Class_Based_Authentication_Article_Single
    Article_List_Viewset,
    # Article_Detail_Viewset
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', Article_List_Viewset, basename='article-list')
# router.register('articles/<int:pk>/', Article_Detail_Viewset, basename='article-detail')

app_name = 'api'



urlpatterns = [

    path('api/', include((router.urls, 'app_name'))),

    # Function based article list view
    # path('', function_based_views_article_list, name='articles'),

    # Function based article single view
    # path('<int:pk>/', function_based_views_article_single, name= 'article_single'),

    # Function based api article list view
    # path('', function_based_api_views_article_list, name='articles'),

    # Function based api article single view
    # path('<int:pk>/', function_based_api_views_article_single, name= 'article_single')

    # Class based api article list view
    # path('', Class_Based_API_Article_List.as_view(), name='articles'),

    # Class based api article single view
    # path('<int:pk>/', Class_Based_API_Article_Single.as_view(), name= 'article_single')

    # Class based api article list view
    # path('', Class_Based_Generic_Api_Article_list.as_view(), name='articles'),

    # Class based api article single view
    # path('<int:pk>/', Class_Based_Generic_Api_Article_Single.as_view(), name= 'article_single')

    # Class based Generic Mixin API article list view
    # path('', Class_Based_Generic_Mixin_API_Article_List.as_view(), name='articles'),

    # Class based Generic Mixin API article single view
    # path('<int:pk>/', Class_Based_Generic_Mixin_API_Article_Single.as_view(), name= 'article_single')

    # Class based Authenticated API article list view
    # path('', Class_Based_Authentication_Article_List.as_view(), name='articles'),

    # Class based Authenticated API article single view
    # path('<int:pk>/', Class_Based_Authentication_Article_Single.as_view(), name= 'article_single')
]
