from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator


class Team(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    photo = models.ImageField(upload_to="photos/team/")
    designation = models.CharField(max_length=100, verbose_name="Designation")
    short_bio = models.TextField(max_length=500)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.TextField(max_length=500)
    about = RichTextField(max_length=1500)
    skill_1 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Skill One"
    )
    skill_1_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Skill One Progress",
    )
    skill_2 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Skill Two"
    )
    skill_2_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Skill Two Progress",
    )
    skill_3 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Skill Three"
    )
    skill_3_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Skill Three Progress",
    )
    skill_4 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Skill Four"
    )
    skill_4_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Skill Four Progress",
    )
    skill_5 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Skill Five"
    )
    skill_5_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Skill Five Progress",
    )
    skill_6 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Skill Six"
    )
    skill_6_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Skill Six Progress",
    )
    skill_7 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Skill Seven"
    )
    skill_7_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Skill Seven Progress",
    )
    skill_8 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Skill Eight"
    )
    skill_8_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Skill Eight Progress",
    )
    skill_9 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Skill Nine"
    )
    skill_9_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Skill Nine Progress",
    )
    skill_10 = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Skill Ten"
    )
    skill_10_progress = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Skill ten Progress",
    )
    year_of_experience = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        blank=True,
        null=True,
        verbose_name="Year of Experience",
    )
    experience_1 = models.TextField(
        max_length=500, blank=True, verbose_name="Experience One"
    )
    experience_2 = models.TextField(
        max_length=500, blank=True, verbose_name="Experience Two"
    )
    experience_3 = models.TextField(
        max_length=500, blank=True, verbose_name="Experience Three"
    )
    experience_4 = models.TextField(
        max_length=500, blank=True, verbose_name="Experience Four"
    )
    experience_5 = models.TextField(
        max_length=500, blank=True, verbose_name="Experience Five"
    )
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    website = models.URLField(blank=True)
    other_website_font_awesome_icon = models.CharField(
        max_length=100, blank=True, verbose_name="Other Website Font Awesome Icon Class"
    )
    other_website_link = models.URLField(blank=True, verbose_name="Other Website Link")
    active_status = models.BooleanField(default=True, verbose_name="Active Status")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"


class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, verbose_name="Designation")
    photo = models.ImageField(upload_to="photos/testimonials/%y%m%d")
    testimonial = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"


class Messages(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=18)
    subject = models.CharField(max_length=500)
    message = models.TextField()
    received_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Received Date"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"


class Clients(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    country = models.CharField(verbose_name="Country", max_length=250)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class Projects(models.Model):
    project_name = models.CharField(max_length=255, verbose_name="Project Name")
    project_description = RichTextField(verbose_name="Project Description")
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    team_member = models.ForeignKey(
        Team, on_delete=models.CASCADE, verbose_name="Associated Team Member"
    )
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
