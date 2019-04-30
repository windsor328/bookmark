"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'bookmark'
urlpatterns = [
    path('', BookmarkList.as_view(), name = 'index'),
    path('create/', BookmarkCreate.as_view(), name = 'create'),
    path('update/<int:pk>', BookmarkUpdate.as_view(), name = 'update'),
    path('delete/<int:pk>', BookmarkDelete.as_view(), name = 'delete'),
    path('detail/<int:pk>', BookmarkDetail.as_view(), name = 'detail'),
    
]
