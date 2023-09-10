"""
URL configuration for MullTab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import index.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('admin/', include('admin.site.urls')),#Админа можно было бы импортировать, так как не главная страница
    path('',views.indexView,name='idx'),
    # path('sign/', include('index.urls')),#Если при открытии сайта мы должны куда то попадать, то зачем нам include?
    # Все равно этот вид будет подгружен сразк.
    path('coderday/', include('coderday.urls')),
    path('mulltable/', include('mulltable.urls')),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
