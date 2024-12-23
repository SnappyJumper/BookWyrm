from django.shortcuts import render
from django.views import generic
from .models import Book, Author
# Create your views here.

class BookList(generic.ListView):
    queryset = Book.objects.all()
    template_name = "book_list.html"

class AuthorList(generic.ListView):
    queryset = Author.objects.all()
    template_name = "author_list.html"