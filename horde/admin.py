from django.contrib import admin
from .models import Author, Book
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    list_display = ("title", "slug", "status")
    search_fields = ["title"]
    list_filter = ("status",)
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("review",)



@admin.register(Author)
class AuthorAdmin(SummernoteModelAdmin):

    list_display = ("name", "nationality", "genre")
    search_fields = ["name"]
    list_filter = ["genre"]
    prepopulated_fields = {"slug_author": ("name",)}
    summernote_fields = ("bio")


# Register your models here.

