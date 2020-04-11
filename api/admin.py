from django.contrib import admin

from api.models import Article

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display       = [ 'title', 'author', 'email', 'created_at']
    list_filter        = [ 'author', 'email']
    list_per_page      = 10
    search_fields      = [ 'title', 'author', 'email' ]

admin.site.register(Article, ArticleAdmin)
