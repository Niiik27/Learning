from django.contrib import admin
from .models import UserProfile
@admin.register(UserProfile)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('user','firstname','secondname','age')
    search_field = ('user__username','firstname','secondname','age')
