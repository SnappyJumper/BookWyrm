from django.shortcuts import render
from django.views import generic
from .models import Book, Author
# Create your views here.

class BookList(generic.ListView):
    queryset = Book.objects.all()
    template_name = "horde/reviews.html"
    paginate_by = 6

class AuthorList(generic.ListView):
    queryset = Author.objects.all()
    template_name = "horde/authors.html"
    paginate_by = 6 

class HomeBookList(generic.ListView):
    queryset = Book.objects.all() 
    template_name = "horde/index.html"
    paginate_by = 6  