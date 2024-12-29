from . import views
from django.urls import path

urlpatterns = [
    path("",views.HomeBookList.as_view(), name="home"),
    path("reviews/", views.BookList.as_view(), name="reviews"),
    path("authors/",views.AuthorList.as_view(), name ="authors"),
    
    path("reviews/<slug:slug>/", views.book_review, name="book_review"),
    path("authors/<slug:slug_author>/", views.author_bio, name="author_bio"),
    
]