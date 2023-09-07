
from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogView, name='blog_in_urls'),
    # path('detail/', views.detailView, name='detail'),
    path('<int:article_id>/', views.detailView, name='detail_in_urls'),
]
