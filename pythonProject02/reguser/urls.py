from django.urls import path
from . import views


urlpatterns = [
    path('', views.loginView, name='login_in_urls'),
    path('registration/', views.regView, name='registration_in_urls'),
]