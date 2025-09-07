from django.urls import path
from .views import *

urlpatterns = [
    path("", index_page, name="index"),
    path("about/", about_page, name="about"),
    path("services/", services_page, name="services"),
    path("contact/", contact_page, name="contact"),
]
