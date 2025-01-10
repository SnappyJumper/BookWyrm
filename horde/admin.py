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
    prepopulated_fields = {"slug": ("title",)} # assigns the slug value to the title value
    summernote_fields = ("review",) # allows the admin to create rich text content in review 



@admin.register(Author)
class AuthorAdmin(SummernoteModelAdmin):
    """
    Contains the fields and filters for the Admin when viewing the Author Model 
    """
    list_display = ("name", "nationality", "genre")
    search_fields = ["name"]
    list_filter = ["genre"]
    prepopulated_fields = {"slug_author": ("name",)} # assigns the slug_author value to the name value
    summernote_fields = ("bio") # allows the admin to create rich text content in bio




