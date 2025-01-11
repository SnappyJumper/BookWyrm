from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Author, Book

# Register your models here.


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):
    """
    Contains the fields and filters for the Admin when viewing the Book Model
    """
    list_display = ("title", "slug", "status")
    search_fields = ["title"]
    list_filter = ("status",)
    # assigns the slug value to the title value
    prepopulated_fields = {"slug": ("title",)}
    # allows the admin to create rich text content in review
    summernote_fields = ("review",)


@admin.register(Author)
class AuthorAdmin(SummernoteModelAdmin):
    """
    Contains the fields and filters for the Admin when viewing the Author Model
    """
    list_display = ("name", "nationality", "genre")
    search_fields = ["name"]
    list_filter = ["genre"]
    # assigns the slug_author value to the name value
    prepopulated_fields = {"slug_author": ("name",)}
    # allows the admin to create rich text content in bio
    summernote_fields = ("bio")
