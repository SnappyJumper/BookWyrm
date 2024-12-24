from . import views
from django.urls import path

urlpatterns = [
    path("", views.BookList.as_view(), name="home"),
    path("reviews/", views.BookList.as_view(), name="reviews"),
    path("authors/",views.AuthorList.as_view(), name ="authors"),
    
]