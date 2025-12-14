"""
URL configuration for my_test project.

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
from django.contrib import admin
from django.urls import path
# from my_site import views
from my_site.views import depart, number, user, admin

urlpatterns = [
    # path("admin/", admin.sites.urls),
    path("depart/list/", depart.depart_list),
    path("depart/add/", depart.depart_add),
    path("depart/delete/", depart.depart_delete),
    path("depart/<int:nid>/edit/", depart.depart_edit),

    path("user/list/", user.user_list),
    path("user/add/", user.user_add),
    path("user/model/form/add/", user.user_model_form_add),
    path("user/<int:nid>/edit/", user.user_edit),
    path("user/<int:nid>/delete/", user.user_delete),

    path("pretty/number/list/", number.pretty_number_list),
    path("pretty/number/add/", number.pretty_number_add),
    path("pretty/number/<int:nid>/edit/", number.pretty_number_edit),
    path("pretty/number/<int:nid>/delete/", number.pretty_number_delete),

    path("admin/list/", admin.admin_list),
    path("admin/add/", admin.admin_add),
]
