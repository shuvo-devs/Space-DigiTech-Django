from django.contrib import admin
from .models import Posts, Comments


class BlogPostsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
        "author_name",
        "published_date",
        "show_on_slider",
    )
    list_display_links = (
        "id",
        "title",
    )
    list_editable = ("show_on_slider",)
    search_fields = (
        "title",
        "category",
        "author_name",
    )


class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "timestamp",
        "post",
        "approved",
    )
    list_editable = ("approved",)
    list_display_links = ("id", "first_name", "last_name")
    readonly_fields = [field.name for field in Comments._meta.fields]
    search_fields = ("id", "first_name", "last_name", "email")

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Posts, BlogPostsAdmin)
admin.site.register(Comments, CommentsAdmin)
