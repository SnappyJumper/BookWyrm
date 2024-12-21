from django.shortcuts import render
from django.views import generic
from .models import Book, Author
# Create your views here.

class BookList(generic.ListView):
    model = Book