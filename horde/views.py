from django.shortcuts import render, get_object_or_404
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

def book_review(request, slug):
    """
    Displays an individual :model:'horde.Book'.

    **Context**
    ''book''
        An instance of :model:'horde.Book'

    **Template**

    :template: 'horde/book_review.html'    
    """

    queryset = Book.objects.filter(status=1)
    book = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "horde/book_review.html",
        {"book": book},
    )

def author_bio(request, slug):
    """
    Displays an individual :model:'horde.Author'.

    **Context**
    ''author''
        An instance of :model:'horde.Author'.
    
    **Template**

    :template: 'horde/author_bio.html
    """

    queryset = Author.objects.filter(status=1)
    author = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "horde/author_bio.html",
        {"author": author},
    )