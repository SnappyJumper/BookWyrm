from . import views
from django.urls import path

urlpatterns = [
    path("",views.HomeBookList.as_view(), name="home"),
    path("reviews/", views.BookList.as_view(), name="reviews"),
    path("authors/",views.AuthorList.as_view(), name ="authors"),
    
    path("reviews/<slug:slug>/", views.book_review, name="book_review"),
    path("reviews/new-review", views.new_review, name="new_review"),
    path("reviews/<slug:slug>/edit-review", views.book_edit, name="book_edit"),
    path("authors/<slug:slug_author>/", views.author_bio, name="author_bio"),
    path("authors/new-author", views.new_author, name="new_author"),
    
]