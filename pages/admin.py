from django.contrib import admin
from .models import (
    WebsiteDetails,
    IndexPage,
    AboutPage,
    ServicesPage,
    TeamPage,
    ContactPage,
)
from solo.admin import SingletonModelAdmin


class WebsiteDetailsAdmin(SingletonModelAdmin):
    fieldsets = [
        (
            "Company",
            {
                "fields": [
                    "site_name",
                    "site_description",
                    "logo_black",
                    "logo_black_alt_text",
                    "logo_white",
                    "logo_white_alt_text",
                    "favicon",
                ],
            },
        ),
        (
            "Contact Details",
            {
                "fields": [
                    "phone_1",
                    "phone_2",
                    "email_1",
                    "email_2",
                    "address",
                    "google_map_location",
                ],
            },
        ),
        (
            "Socials",
            {
                "fields": [
                    "facebook",
                    "twitter",
                    "instagram",
                    "youtube",
                    "pinterest",
                    "linkedin",
                    "whatsapp",
                    "skype",
                ],
            },
        ),
    ]


class IndexPageAdmin(SingletonModelAdmin):
    fieldsets = [
        (
            "About Section",
            {
                "fields": [
                    "about_section_heading",
                    "about_section_text",
                    "about_section_image",
                    "about_section_image_alt_text",
                ],
            },
        ),
        (
            "Services Section",
            {
                "fields": [
                    "services_section_heading",
                ],
            },
        ),
        (
            "Features Section",
            {
                "fields": [
                    "features_section_title",
                    "features_section_heading",
                    "features_section_image",
                    "features_section_image_alt_text",
                    "feature_bullet_1",
                    "feature_bullet_2",
                    "feature_bullet_3",
                ],
            },
        ),
        (
            "Best Services Section",
            {
                "fields": [
                    "best_services_section_text",
                    "best_service_1_font_awesome_icon",
                    "best_service_1_heading",
                    "best_service_1_text",
                    "best_service_1_page_link",
                    "best_service_2_font_awesome_icon",
                    "best_service_2_heading",
                    "best_service_2_text",
                    "best_service_2_page_link",
                    "best_service_3_font_awesome_icon",
                    "best_service_3_heading",
                    "best_service_3_text",
                    "best_service_3_page_link",
                ],
            },
        ),
        (
            "Our Company Section",
            {
                "fields": [
                    "our_company_section_title",
                    "our_company_section_heading",
                    "our_company_section_text",
                    "our_company_section_image",
                    "our_company_section_image_alt_text",
                    "our_company_bullet_1",
                    "our_company_bullet_2",
                    "our_company_bullet_3",
                    "our_company_bullet_4",
                    "our_company_bullet_5",
                ],
            },
        ),
        (
            "Counter Section",
            {
                "fields": [
                    "counter_section_text",
                    "counter_1_title",
                    "counter_1_progress",
                    "counter_2_title",
                    "counter_2_progress",
                    "counter_3_title",
                    "counter_3_progress",
                    "counter_4_title",
                    "counter_4_progress",
                ],
            },
        ),
        (
            "Skills Section",
            {
                "fields": [
                    "our_skills_heading",
                    "our_skills_text",
                    "our_skills_image",
                    "our_skills_image_alt_text",
                    "our_skill_1",
                    "our_skill_1_progress",
                    "our_skill_2",
                    "our_skill_2_progress",
                    "our_skill_3",
                    "our_skill_3_progress",
                    "our_skill_4",
                    "our_skill_4_progress",
                    "our_skill_5",
                    "our_skill_5_progress",
                    "our_skill_6",
                    "our_skill_6_progress",
                    "our_skill_7",
                    "our_skill_7_progress",
                    "our_skill_8",
                    "our_skill_8_progress",
                    "our_skill_9",
                    "our_skill_9_progress",
                    "our_skill_10",
                    "our_skill_10_progress",
                ],
            },
        ),
    ]


class AboutPageAdmin(SingletonModelAdmin):
    pass


class ServicesPageAdmin(SingletonModelAdmin):
    pass


class TeamPageAdmin(SingletonModelAdmin):
    pass


class ContactPageAdmin(SingletonModelAdmin):
    pass


admin.site.register(WebsiteDetails, WebsiteDetailsAdmin)
admin.site.register(IndexPage, IndexPageAdmin)
admin.site.register(AboutPage, AboutPageAdmin)
admin.site.register(ServicesPage, ServicesPageAdmin)
admin.site.register(TeamPage, TeamPageAdmin)
admin.site.register(ContactPage, ContactPageAdmin)
