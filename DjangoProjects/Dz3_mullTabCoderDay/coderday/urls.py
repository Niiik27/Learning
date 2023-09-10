
from django.urls import path
import coderday.views

urlpatterns = [
    path('coderday/', coderday.views.coderdayView,name='action_coderday'),
]
