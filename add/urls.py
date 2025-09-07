from django.urls import path
from .views import *

urlpatterns = [
    path("service/<slug:services_slug>/", service_details, name="service_details"),
    path(
        "service/<slug:services_slug>/<slug:subservices_slug>/",
        sub_service_details,
        name="service_details",
    ),
    path(
        "service/<slug:services_slug>/<slug:subservices_slug>/<slug:subsubservices_slug>/",
        sub_sub_service_details,
        name="service_details",
    ),
]
