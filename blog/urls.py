from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("blog/", blog, name="blog"),
    path("category/<str:category_slug>", category, name="category"),
    path(
        "category/<str:category_slug>/<str:post_slug>/",
        post_details,
        name="post_details",
    ),
]
