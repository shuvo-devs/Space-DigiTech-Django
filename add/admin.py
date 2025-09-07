from django.contrib import admin
from .models import Services, SubServices, SubSubServices, Category, Slider
from django.utils.html import format_html


class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        "sl_no",
        "service_name",
        "show_on_homepage",
        "sub_menu",
    )
    list_display_links = (
        "sl_no",
        "service_name",
    )
    list_editable = (
        "show_on_homepage",
        "sub_menu",
    )


class SubSubServicesInline(admin.StackedInline):
    model = SubSubServices
    extra = 0


class SubServicesAdmin(admin.ModelAdmin):
    inlines = [
        SubSubServicesInline,
    ]
    fieldsets = [
        (
            "Sub Service",
            {
                "fields": [
                    "service",
                    "sl_no",
                    "service_name",
                    "service_description",
                    "slug",
                    "icon_for_services_page",
                    "service_heading",
                    "service_image",
                    "service_image_alt_text",
                    "service_point_1_heading",
                    "service_point_1_description",
                    "service_point_2_heading",
                    "service_point_2_description",
                    "service_point_3_heading",
                    "service_point_3_description",
                    "service_point_4_heading",
                    "service_point_4_description",
                    "service_feature_1_heading",
                    "service_feature_1_sub_heading",
                    "service_feature_2_heading",
                    "service_feature_2_sub_heading",
                    "service_feature_3_heading",
                    "service_feature_3_sub_heading",
                    "sub_menu",
                ]
            },
        )
    ]
    list_display = (
        "sl_no",
        "service_name",
        "sub_menu",
    )
    list_display_links = (
        "sl_no",
        "service_name",
    )
    list_editable = ("sub_menu",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "featured_category")
    list_display_links = ("name",)
    list_editable = ("featured_category",)


class SliderAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(
            "<img src={} style='border-radius: 5px' width='50px'/>".format(
                object.slider_image.url
            )
        )

    thumbnail.short_description = "Slider Image"
    list_display = ("thumbnail", "title", "hire_us_btn")
    list_display_links = (
        "thumbnail",
        "title",
    )
    list_editable = ("hire_us_btn",)


admin.site.register(Services, ServicesAdmin)
admin.site.register(SubServices, SubServicesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Slider, SliderAdmin)
