from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from solo.models import SingletonModel


class WebsiteDetails(SingletonModel):
    site_name = models.CharField(max_length=100, blank=True, verbose_name="Site Name")
    site_description = RichTextField(
        max_length=500, blank=True, verbose_name="Site Description"
    )
    logo_black = models.ImageField(
        upload_to="photos/website/", blank=True, verbose_name="Logo Black"
    )
    logo_black_alt_text = models.CharField(
        blank=True, verbose_name="Logo Black Alt Text", max_length=250
    )
    logo_white = models.ImageField(
        upload_to="photos/website/", blank=True, verbose_name="Logo White"
    )
    logo_white_alt_text = models.CharField(
        blank=True, verbose_name="Logo White Alt Text", max_length=250
    )
    favicon = models.ImageField(upload_to="photos/website/", blank=True)
    phone_1 = models.CharField(max_length=50, blank=True, verbose_name="Phone One")
    phone_2 = models.CharField(max_length=50, blank=True, verbose_name="Phone Two")
    email_1 = models.EmailField(blank=True, verbose_name="Email One")
    email_2 = models.EmailField(blank=True, verbose_name="Email Two")
    address = models.CharField(max_length=250, blank=True)
    google_map_location = models.TextField(blank=True, verbose_name="Google Maps API")
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    pinterest = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    whatsapp = models.URLField(blank=True)
    skype = models.URLField(blank=True)

    class Meta:
        verbose_name = "Website Details"

    def __str__(self):
        return self.site_name


class IndexPage(SingletonModel):
    about_section_heading = models.TextField(
        max_length=500, blank=True, verbose_name="Heading"
    )
    about_section_text = models.TextField(
        max_length=500, blank=True, verbose_name="Text"
    )
    about_section_image = models.ImageField(
        upload_to="photos/index_page/", blank=True, verbose_name="Image"
    )
    about_section_image_alt_text = models.CharField(
        blank=True, verbose_name="Image Alt Text", max_length=250
    )

    services_section_heading = models.TextField(
        max_length=500, blank=True, verbose_name="Heading"
    )

    features_section_title = models.TextField(
        max_length=250, blank=True, verbose_name="Title"
    )
    features_section_heading = models.TextField(
        max_length=500, blank=True, verbose_name="Heading"
    )
    features_section_image = models.ImageField(
        upload_to="photos/index_page/", blank=True, verbose_name="Image"
    )
    features_section_image_alt_text = models.CharField(
        blank=True, verbose_name="Image Alt Text", max_length=250
    )
    feature_bullet_1 = models.TextField(
        max_length=500, blank=True, verbose_name="Bullet One"
    )
    feature_bullet_2 = models.TextField(
        max_length=500, blank=True, verbose_name="Bullet Two"
    )
    feature_bullet_3 = models.TextField(
        max_length=500, blank=True, verbose_name="Bullet Three"
    )

    best_services_section_text = models.TextField(
        max_length=500, blank=True, verbose_name="Section Text"
    )
    best_service_1_font_awesome_icon = models.CharField(
        max_length=100, blank=True, verbose_name="Service One Font Awesome Icon Tag"
    )
    best_service_1_heading = models.CharField(
        max_length=100, blank=True, verbose_name="Service One Heading"
    )
    best_service_1_text = models.TextField(
        max_length=250, blank=True, verbose_name="Service One Text"
    )
    best_service_1_page_link = models.CharField(
        blank=True, verbose_name="Service One Page Link", max_length=250
    )
    best_service_2_font_awesome_icon = models.CharField(
        max_length=100, blank=True, verbose_name="Service Two Font Awesome Icon Tag"
    )
    best_service_2_heading = models.CharField(
        max_length=100, blank=True, verbose_name="Service Two Heading"
    )
    best_service_2_text = models.TextField(
        max_length=250, blank=True, verbose_name="Service Two Text"
    )
    best_service_2_page_link = models.CharField(
        blank=True, verbose_name="Service Two Page Link", max_length=250
    )
    best_service_3_font_awesome_icon = models.CharField(
        max_length=100, blank=True, verbose_name="Service Three Font Awesome Icon Tag"
    )
    best_service_3_heading = models.CharField(
        max_length=100, blank=True, verbose_name="Service Three Heading"
    )
    best_service_3_text = models.TextField(
        max_length=250, blank=True, verbose_name="Service Three Text"
    )
    best_service_3_page_link = models.CharField(
        blank=True, verbose_name="Service Three Page Link", max_length=250
    )

    our_company_section_title = models.TextField(
        max_length=250, blank=True, verbose_name="Title"
    )
    our_company_section_heading = models.TextField(
        max_length=250, blank=True, verbose_name="Heading"
    )
    our_company_section_text = models.TextField(
        max_length=500, blank=True, verbose_name="Text"
    )
    our_company_section_image = models.ImageField(
        upload_to="photos/index_page/", blank=True, verbose_name="Image"
    )
    our_company_section_image_alt_text = models.CharField(
        blank=True, verbose_name="Image Alt Text", max_length=250
    )
    our_company_bullet_1 = models.CharField(
        max_length=500, blank=True, verbose_name="Bullet One"
    )
    our_company_bullet_2 = models.CharField(
        max_length=500, blank=True, verbose_name="Bullet Twp"
    )
    our_company_bullet_3 = models.CharField(
        max_length=500, blank=True, verbose_name="Bullet Three"
    )
    our_company_bullet_4 = models.CharField(
        max_length=500, blank=True, verbose_name="Bullet Four"
    )
    our_company_bullet_5 = models.CharField(
        max_length=500, blank=True, verbose_name="Bullet Five"
    )

    counter_section_text = models.CharField(
        max_length=250, blank=True, verbose_name="Section Text"
    )
    counter_1_title = models.CharField(
        max_length=100, blank=True, verbose_name="Counter One Title"
    )
    counter_1_progress = models.IntegerField(
        blank=True, verbose_name="Counter One Progress", null=True
    )
    counter_2_title = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Counter Two Title",
    )
    counter_2_progress = models.IntegerField(
        blank=True, verbose_name="Counter Two Progress", null=True
    )
    counter_3_title = models.CharField(
        max_length=100, blank=True, verbose_name="Counter Three Title"
    )
    counter_3_progress = models.IntegerField(
        blank=True, verbose_name="Counter Three Progress", null=True
    )
    counter_4_title = models.CharField(
        max_length=100, blank=True, verbose_name="Counter Four Title"
    )
    counter_4_progress = models.IntegerField(
        blank=True, verbose_name="Counter Four Progress", null=True
    )

    our_skills_heading = models.TextField(
        max_length=500, blank=True, verbose_name="Heading"
    )
    our_skills_text = models.TextField(max_length=500, blank=True, verbose_name="Text")
    our_skills_image = models.ImageField(
        upload_to="photos/index_page/", blank=True, verbose_name="Image"
    )
    our_skills_image_alt_text = models.CharField(
        blank=True, verbose_name="Image Alt Text", max_length=250
    )
    our_skill_1 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Skill One"
    )
    our_skill_1_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Skill One Progress",
    )
    our_skill_2 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Skill Two"
    )
    our_skill_2_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Skill Two Progress",
    )
    our_skill_3 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Skill Three"
    )
    our_skill_3_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Skill Three Progress",
    )
    our_skill_4 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Skill Four"
    )
    our_skill_4_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Skill Four Progress",
    )
    our_skill_5 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Skill Five"
    )
    our_skill_5_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Skill Five Progress",
    )
    our_skill_6 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Skill Six"
    )
    our_skill_6_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Skill Six Progress",
    )
    our_skill_7 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Skill Seven"
    )
    our_skill_7_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Skill Seven Progress",
    )
    our_skill_8 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Skill Eight"
    )
    our_skill_8_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Skill Eight Progress",
    )
    our_skill_9 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Skill Nine"
    )
    our_skill_9_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Skill Nine Progress",
    )
    our_skill_10 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Skill Ten"
    )
    our_skill_10_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Skill Ten Progress",
    )

    class Meta:
        verbose_name = "Index Page"
        verbose_name_plural = "Index Page"

    page_name = "Index Page"

    def __str__(self):
        return self.page_name


class AboutPage(SingletonModel):
    page_title = models.CharField(max_length=100, blank=True, verbose_name="Page Title")
    page_text = models.TextField(max_length=250, blank=True, verbose_name="Page Text")
    page_title_image = models.ImageField(
        upload_to="photos/about_page/", blank=True, verbose_name="Page Title Image"
    )
    page_title_image_alt_text = models.CharField(
        blank=True, verbose_name="Page Title Image Alt Text", max_length=250
    )
    section_image = models.ImageField(
        upload_to="photos/about_page/", blank=True, verbose_name="Section Image"
    )
    section_image_alt_text = models.CharField(
        blank=True, verbose_name="Section Image Alt Text", max_length=250
    )
    experience = models.IntegerField(blank=True, null=True)
    award_title = models.CharField(
        max_length=250, blank=True, verbose_name="Award Title"
    )
    award_description = models.TextField(
        max_length=250, blank=True, verbose_name="Award Description"
    )
    section_heading = models.TextField(
        max_length=500, blank=True, verbose_name="Section Heading"
    )
    section_text = models.TextField(
        max_length=500, blank=True, verbose_name="Section Text"
    )
    our_mission = RichTextField(max_length=500, blank=True, verbose_name="Our Mission")
    our_vision = RichTextField(max_length=500, blank=True, verbose_name="Our Vision")
    our_value = RichTextField(max_length=500, blank=True, verbose_name="Our Value")

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"

    page_name = "About Page"

    def __str__(self):
        return self.page_name


class ServicesPage(SingletonModel):
    page_title = models.CharField(max_length=100, blank=True, verbose_name="Page Title")
    page_text = models.TextField(max_length=250, blank=True, verbose_name="Page Text")
    section_heading = models.TextField(
        max_length=500, blank=True, verbose_name="Section Heading"
    )
    section_text = models.TextField(
        max_length=500, blank=True, verbose_name="Section Text"
    )

    class Meta:
        verbose_name = "Services Page"
        verbose_name_plural = "Services Page"

    page_name = "Services Page"

    def __str__(self):
        return self.page_name


class TeamPage(SingletonModel):
    page_title = models.CharField(max_length=100, blank=True, verbose_name="Page Title")
    page_text = models.TextField(max_length=250, blank=True, verbose_name="Page Text")

    class Meta:
        verbose_name = "Team Page"
        verbose_name_plural = "Team Page"

    page_name = "Team Page"

    def __str__(self):
        return self.page_name


class ContactPage(SingletonModel):
    page_title = models.CharField(max_length=100, blank=True, verbose_name="Page Title")
    page_text = models.TextField(max_length=250, blank=True, verbose_name="Page Text")
    section_heading = models.TextField(
        max_length=500, blank=True, verbose_name="Heading"
    )
    section_text = models.TextField(max_length=500, blank=True, verbose_name="Text")

    class Meta:
        verbose_name = "Contact Page"
        verbose_name_plural = "Contact Page"

    page_name = "Contact Page"

    def __str__(self):
        return self.page_name
