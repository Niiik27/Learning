from django.urls import path
from . import views


urlpatterns = [
    path('', views.inputsView, name='inputs_in_urls'),
]