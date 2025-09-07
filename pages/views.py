from django.shortcuts import render, redirect
from .models import (
    IndexPage,
    AboutPage,
    ServicesPage,
    ContactPage,
)
from add.models import Services, SubServices, SubSubServices, Slider
from clients_teams_projects.models import Team, Testimonials, Messages
from blog.models import Posts


def index_page(request):
    try:
        index_page = IndexPage.get_solo()
    except IndexPage.DoesNotExist:
        index_page = None

    slider = Slider.objects.all()
    team = Team.objects.all()
    testimonials = Testimonials.objects.all()
    posts = Posts.objects.all()

    data = {
        "index_page": index_page,
        "slider": slider,
        "team": team,
        "testimonials": testimonials,
        "posts": posts,
    }

    return render(request, "pages/index.html", data)


def about_page(request):
    try:
        about_page = AboutPage.get_solo()
    except AboutPage.DoesNotExist:
        about_page = None

    data = {
        "about_page": about_page,
    }
    return render(request, "pages/about.html", data)


def services_page(request):
    try:
        services_page = ServicesPage.get_solo()
    except ServicesPage.DoesNotExist:
        services_page = None

    services = Services.objects.order_by("sl_no")
    sub_services = SubServices.objects.order_by("sl_no")
    sub_sub_services = SubSubServices.objects.order_by("sl_no")

    data = {
        "services_page": services_page,
        "services": services,
        "sub_services": sub_services,
        "sub_sub_services": sub_sub_services,
    }
    return render(request, "pages/services.html", data)


def contact_page(request):
    try:
        contact_page = ContactPage.get_solo()
    except ContactPage.DoesNotExist:
        contact_page = None

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        send_message = Messages(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message,
        )
        send_message.save()
        return redirect("contact")

    data = {
        "contact_page": contact_page,
    }
    return render(request, "pages/contact.html", data)
