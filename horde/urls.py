from . import views
from django.urls import path

urlpatterns = [
    path("reviews/", views.BookList.as_view(), name="reviews"),
    path("authors/",views.AuthorList.as_view(), name ="authors")
]