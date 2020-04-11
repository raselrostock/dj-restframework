from django.db import models

class Article(models.Model):
    title      = models.CharField(max_length=128)
    author     = models.CharField(max_length=64)
    email      = models.EmailField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'article'
        verbose_name_plural = 'articles'
        ordering            = ['created_at']


    def __str__(self):
        return self.title
    
