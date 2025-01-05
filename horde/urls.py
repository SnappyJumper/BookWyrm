from . import views
from django.urls import path

urlpatterns = [
    path("",views.HomeBookList.as_view(), name="home"),
    path("reviews/", views.BookList.as_view(), name="reviews"),
    path("authors/",views.AuthorList.as_view(), name ="authors"),
    
    path("reviews/<slug:slug>/", views.book_review, name="book_review"),
    path("reviews/new-review", views.AddReview.as_view(), name="new_review"),
    path("reviews/<slug:slug>/edit-review", views.book_edit, name="book_edit"),
    path("reviews/<slug:slug>/delete-review", views.book_delete, name ="book_delete" ),
    path("authors/<slug:slug_author>/", views.author_bio, name="author_bio"),
    path("authors/new-author", views.AddAuthor.as_view(), name="new_author"),
    path("authors/<slug:slug_author>/edit-author", views.author_edit, name="author_edit"),
    path("authors/<slug:slug_author>/delete-author", views.author_delete, name="author_delete"),
]