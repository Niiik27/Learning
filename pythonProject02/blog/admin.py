from django.apps import AppConfig
from django.contrib import admin
from .models import Article

# Register your models here.
# admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','date')

