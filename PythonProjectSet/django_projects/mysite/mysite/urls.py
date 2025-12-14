"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app1 import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("index/", views.index),
    path("tpl/", views.test_templates),
    path("news/", views.unicom_news),
    path("some/", views.something),
    path("login/", views.user_login),
    path("orm/", views.test_orm),
    path("info/list/", views.info_list),
    path("info/add/", views.info_add),
    path("info/del/", views.info_del),
]
