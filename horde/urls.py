from . import views
from django.urls import path

urlpatterns = [
    path("",views.HomeBookList.as_view(), name="home"), # Home URL
    path("reviews/", views.BookList.as_view(), name="reviews"), # Reviews URL
    path("reviews/<slug:slug>/", views.book_review, name="book_review"), # Book Review URL
    path("reviews/new-review", views.AddReview.as_view(), name="new_review"), # New Review URL
    path("reviews/<slug:slug>/edit-review", views.book_edit, name="book_edit"), # Edit Review URL
    path("reviews/<slug:slug>/delete-review", views.book_delete, name ="book_delete" ), # Delete Review URL
    path("authors/",views.AuthorList.as_view(), name ="authors"), # Authors URL
    path("authors/<slug:slug_author>/", views.author_bio, name="author_bio"), # Author Bio URL
    path("authors/new-author", views.AddAuthor.as_view(), name="new_author"), # New Author URL
    path("authors/<slug:slug_author>/edit-author", views.author_edit, name="author_edit"), # Edit Author URL
    path("authors/<slug:slug_author>/delete-author", views.author_delete, name="author_delete"), # Delete Author URL
]