from django.contrib import admin
from .models import Team, Testimonials, Messages, Clients, Projects
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(
            "<img src={} style='border-radius: 5px' width='50px'/>".format(
                object.photo.url
            )
        )

    thumbnail.short_description = "Photo"
    list_display = (
        "id",
        "thumbnail",
        "name",
        "designation",
        "email",
        "phone",
        "active_status",
        "created_date",
    )
    list_display_links = (
        "id",
        "thumbnail",
        "name",
    )
    list_editable = ("active_status",)
    list_filter = ("id", "designation", "active_status")
    search_fields = (
        "id",
        "name",
        "designation",
    )
    fieldsets = [
        (
            "Personal Information",
            {
                "fields": [
                    "name",
                    "slug",
                    "photo",
                    "designation",
                    "short_bio",
                    "email",
                    "phone",
                    "address",
                    "about",
                ],
            },
        ),
        (
            "Skills",
            {
                "fields": [
                    "skill_1",
                    "skill_1_progress",
                    "skill_2",
                    "skill_2_progress",
                    "skill_3",
                    "skill_3_progress",
                    "skill_4",
                    "skill_4_progress",
                    "skill_5",
                    "skill_5_progress",
                    "skill_6",
                    "skill_6_progress",
                    "skill_7",
                    "skill_7_progress",
                    "skill_8",
                    "skill_8_progress",
                    "skill_9",
                    "skill_9_progress",
                    "skill_10",
                    "skill_10_progress",
                ],
            },
        ),
        (
            "Experiences",
            {
                "fields": [
                    "year_of_experience",
                    "experience_1",
                    "experience_2",
                    "experience_3",
                    "experience_4",
                    "experience_5",
                ],
            },
        ),
        (
            "Socials",
            {
                "fields": [
                    "facebook",
                    "instagram",
                    "twitter",
                    "youtube",
                    "linkedin",
                    "website",
                    "other_website_font_awesome_icon",
                    "other_website_link",
                ],
            },
        ),
        (
            "Status",
            {
                "fields": [
                    "active_status",
                ],
            },
        ),
    ]


class TestimonialsAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(
            "<img src={} style='border-radius: 5px' width='50px'/>".format(
                object.photo.url
            )
        )

    thumbnail.short_description = "Photo"
    list_display = (
        "id",
        "thumbnail",
        "name",
        "designation",
        "created_date",
    )
    list_display_links = (
        "id",
        "thumbnail",
        "name",
    )
    search_fields = (
        "id",
        "name",
        "designation",
    )
    list_filter = (
        "id",
        "designation",
    )


class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "subject", "email", "phone")
    list_display_links = (
        "id",
        "name",
    )
    search_fields = ("id", "name", "email", "phone")
    readonly_fields = [field.name for field in Messages._meta.fields]

    def has_add_permission(self, request, obj=None):
        return False


class ClientsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "country",
        "created_date",
    )
    list_display_links = (
        "id",
        "name",
        "email",
    )
    search_fields = (
        "id",
        "name",
        "email",
        "phone",
        "country",
    )
    list_filter = ("country",)


class ProjectsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "project_name",
        "client",
        "team_member",
        "created_date",
    )
    list_display_links = (
        "id",
        "project_name",
    )
    search_fields = (
        "id",
        "project_name",
        "project_description",
        "client",
        "team_member",
    )
    list_filter = (
        "client",
        "team_member",
    )


admin.site.register(Team, TeamAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)
admin.site.register(Messages, MessageAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Clients, ClientsAdmin)
