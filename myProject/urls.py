from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from backend_api.views import *

urlpatterns = [
    path("", admin.site.urls),
    path("get_categories/", get_categories, name="get_categories"),
    path("categories/", Categories.as_view(), name="categories"),
    path("login_view/", login_view, name="login_view"),
    path('register/', register_user_view, name='register_user'),
    path('projectInformations/', projectInformations, name='projectInformations'),
]
