from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

import mulltable.views
urlpatterns = [
    path('', mulltable.views.mulltabView,name='action_mulltab'),
]