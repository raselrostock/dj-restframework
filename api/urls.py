from django.urls import path
from api.views import function_based_views

app_name = 'api'

urlpatterns = [
    path('', function_based_views, name='articles')
]
