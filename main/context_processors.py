from pages.models import WebsiteDetails
from add.models import Services, SubServices, SubSubServices, Category


def website_details(request):
    try:
        website_details = WebsiteDetails.get_solo()
    except WebsiteDetails.DoesNotExist:
        website_details = None

    data = {
        "website_details": website_details,
    }

    return data


def add(request):
    try:
        services = Services.objects.all()
    except Services.DoesNotExist:
        services = None

    try:
        sub_services = SubServices.objects.all()
    except SubServices.DoesNotExist:
        sub_services = None

    try:
        sub_sub_services = SubSubServices.objects.all()
    except SubSubServices.DoesNotExist:
        sub_sub_services = None

    try:
        categories = Category.objects.all()
    except Category.DoesNotExist:
        categories = None

    data = {
        "services": services,
        "sub_services": sub_services,
        "sub_sub_services": sub_sub_services,
        "categories": categories,
    }

    return data
