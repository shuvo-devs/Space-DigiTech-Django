from django.db import models
from ckeditor.fields import RichTextField


class Services(models.Model):
    sl_no = models.CharField(verbose_name="Service No.", max_length=250)
    service_name = models.CharField(max_length=100, verbose_name="Service Name")
    service_description = RichTextField(
        max_length=250, verbose_name="Service Description"
    )
    slug = models.SlugField(unique=True)
    icon_for_homepage = models.ImageField(
        upload_to="photos/services/",
        blank=True,
        verbose_name="Icon for Homepage",
    )
    icon_for_services_page = models.ImageField(
        upload_to="photos/services/",
        verbose_name="Icon for Services Page",
    )
    service_heading = models.TextField(max_length=500, verbose_name="Service Heading")
    service_image = models.ImageField(
        upload_to="photos/services/", verbose_name="Service Photo"
    )
    service_image_alt_text = models.CharField(
        verbose_name="Service Image Alt Text", max_length=250
    )
    service_point_1_heading = models.CharField(
        max_length=100, verbose_name="Service Point One", blank=True
    )
    service_point_1_description = models.TextField(
        max_length=250, verbose_name="Point One Description", blank=True
    )
    service_point_2_heading = models.CharField(
        max_length=100, verbose_name="Service Point Two", blank=True
    )
    service_point_2_description = models.TextField(
        max_length=250, verbose_name="Point Two Description", blank=True
    )
    service_point_3_heading = models.CharField(
        max_length=100, verbose_name="Service Point Three", blank=True
    )
    service_point_3_description = models.TextField(
        max_length=250, verbose_name="Point Three Description", blank=True
    )
    service_point_4_heading = models.CharField(
        max_length=100, verbose_name="Service Point Four", blank=True
    )
    service_point_4_description = models.TextField(
        max_length=250, verbose_name="Point Four Description", blank=True
    )
    service_feature_1_heading = models.CharField(
        max_length=100, verbose_name="Service Feature One Heading"
    )
    service_feature_1_sub_heading = models.CharField(
        max_length=100, verbose_name="Feature One Sub-Heading"
    )
    service_feature_2_heading = models.CharField(
        max_length=100, verbose_name="Service Feature Two Heading"
    )
    service_feature_2_sub_heading = models.CharField(
        max_length=100, verbose_name="Feature Two Sub-Heading"
    )
    service_feature_3_heading = models.CharField(
        max_length=100, verbose_name="Service Feature Three Heading"
    )
    service_feature_3_sub_heading = models.CharField(
        max_length=100, verbose_name="Feature Three Sub-Heading"
    )
    show_on_homepage = models.BooleanField(
        default=False, verbose_name="Show on Homepage"
    )
    sub_menu = models.BooleanField(default=False, verbose_name="Enable Sub-Menu")

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class SubServices(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    sl_no = models.CharField(verbose_name="Service No.", max_length=250)
    service_name = models.CharField(max_length=100, verbose_name="Service Name")
    service_description = RichTextField(
        max_length=250, verbose_name="Service Description"
    )
    slug = models.SlugField(unique=True)
    icon_for_services_page = models.ImageField(
        upload_to="photos/services/",
        verbose_name="Icon for Services Page",
    )
    service_heading = models.TextField(max_length=500, verbose_name="Service Heading")
    service_image = models.ImageField(
        upload_to="photos/services/", verbose_name="Service Photo"
    )
    service_image_alt_text = models.CharField(
        verbose_name="Service Image Alt Text", max_length=250
    )
    service_point_1_heading = models.CharField(
        max_length=100, verbose_name="Service Point One", blank=True
    )
    service_point_1_description = models.TextField(
        max_length=250, verbose_name="Point One Description", blank=True
    )
    service_point_2_heading = models.CharField(
        max_length=100, verbose_name="Service Point Two", blank=True
    )
    service_point_2_description = models.TextField(
        max_length=250, verbose_name="Point Two Description", blank=True
    )
    service_point_3_heading = models.CharField(
        max_length=100, verbose_name="Service Point Three", blank=True
    )
    service_point_3_description = models.TextField(
        max_length=250, verbose_name="Point Three Description", blank=True
    )
    service_point_4_heading = models.CharField(
        max_length=100, verbose_name="Service Point Four", blank=True
    )
    service_point_4_description = models.TextField(
        max_length=250, verbose_name="Point Four Description", blank=True
    )
    service_feature_1_heading = models.CharField(
        max_length=100, verbose_name="Service Feature One Heading"
    )
    service_feature_1_sub_heading = models.CharField(
        max_length=100, verbose_name="Feature One Sub-Heading"
    )
    service_feature_2_heading = models.CharField(
        max_length=100, verbose_name="Service Feature Two Heading"
    )
    service_feature_2_sub_heading = models.CharField(
        max_length=100, verbose_name="Feature Two Sub-Heading"
    )
    service_feature_3_heading = models.CharField(
        max_length=100, verbose_name="Service Feature Three Heading"
    )
    service_feature_3_sub_heading = models.CharField(
        max_length=100, verbose_name="Feature Three Sub-Heading"
    )
    sub_menu = models.BooleanField(default=False, verbose_name="Enable Sub-Menu")

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = "Sub Service"
        verbose_name_plural = "Sub Services"


class SubSubServices(models.Model):
    sub_service = models.ForeignKey(SubServices, on_delete=models.CASCADE)
    sl_no = models.CharField(verbose_name="Service No.", max_length=250)
    service_name = models.CharField(max_length=100, verbose_name="Service Name")
    service_description = RichTextField(
        max_length=250, verbose_name="Service Description"
    )
    slug = models.SlugField(unique=True)
    icon_for_services_page = models.ImageField(
        upload_to="photos/services/",
        verbose_name="Icon for Services Page",
    )
    service_heading = models.TextField(max_length=500, verbose_name="Service Heading")
    service_image = models.ImageField(
        upload_to="photos/services/", verbose_name="Service Photo"
    )
    service_image_alt_text = models.CharField(
        verbose_name="Service Image Alt Text", max_length=250
    )
    service_point_1_heading = models.CharField(
        max_length=100, verbose_name="Service Point One", blank=True
    )
    service_point_1_description = models.TextField(
        max_length=250, verbose_name="Point One Description", blank=True
    )
    service_point_2_heading = models.CharField(
        max_length=100, verbose_name="Service Point Two", blank=True
    )
    service_point_2_description = models.TextField(
        max_length=250, verbose_name="Point Two Description", blank=True
    )
    service_point_3_heading = models.CharField(
        max_length=100, verbose_name="Service Point Three", blank=True
    )
    service_point_3_description = models.TextField(
        max_length=250, verbose_name="Point Three Description", blank=True
    )
    service_point_4_heading = models.CharField(
        max_length=100, verbose_name="Service Point Four", blank=True
    )
    service_point_4_description = models.TextField(
        max_length=250, verbose_name="Point Four Description", blank=True
    )
    service_feature_1_heading = models.CharField(
        max_length=100, verbose_name="Service Feature One Heading"
    )
    service_feature_1_sub_heading = models.CharField(
        max_length=100, verbose_name="Feature One Sub-Heading"
    )
    service_feature_2_heading = models.CharField(
        max_length=100, verbose_name="Service Feature Two Heading"
    )
    service_feature_2_sub_heading = models.CharField(
        max_length=100, verbose_name="Feature Two Sub-Heading"
    )
    service_feature_3_heading = models.CharField(
        max_length=100, verbose_name="Service Feature Three Heading"
    )
    service_feature_3_sub_heading = models.CharField(
        max_length=100, verbose_name="Feature Three Sub-Heading"
    )

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = "Sub-Sub Service"
        verbose_name_plural = "Sub-Sub Services"


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    featured_category = models.BooleanField(
        default=False, verbose_name="Featured Category"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Slider(models.Model):
    slider_image = models.ImageField(
        upload_to="photos/index_page/slider/", verbose_name="Slider Image"
    )
    slider_image_alt_text = models.CharField(
        verbose_name="Slider Image Alt Text", max_length=250
    )
    title = models.CharField(max_length=250)
    heading = models.TextField(max_length=500)
    text = RichTextField(max_length=500)
    hire_us_btn = models.BooleanField(
        default=False, verbose_name="Enable Hire Us Button"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Index Slider"
