
from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogView, name='blog'),
    path('detail/', views.detailView, name='detail'),
    path('<int:article_id>/', views.detailView, name='detail'),
]
