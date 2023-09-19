from django.urls import path
from . import views


urlpatterns = [
    path('', views.loginuserView, name='login_in_urls'),
    path('registration/', views.reguserView, name='registration_in_urls'),
    path('logout/', views.logoutuserView, name='logoutuser'),
    path('profile/', views.profileView, name='profile'),
    path('profileup/', views.profileupView, name='profileup'),
]