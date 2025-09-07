from django.shortcuts import render, get_object_or_404
from .models import Services, SubServices, SubSubServices


def service_details(request, services_slug):
    service_details = get_object_or_404(Services, slug=services_slug)

    data = {
        "service_details": service_details,
    }
    return render(request, "pages/service_details.html", data)


def sub_service_details(request, services_slug, subservices_slug):
    service_details = get_object_or_404(SubServices, slug=subservices_slug)

    data = {
        "service_details": service_details,
    }
    return render(request, "pages/service_details.html", data)


def sub_sub_service_details(
    request, services_slug, subservices_slug, subsubservices_slug
):
    service_details = get_object_or_404(SubSubServices, slug=subsubservices_slug)

    data = {
        "service_details": service_details,
    }
    return render(request, "pages/service_details.html", data)
