from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book, Author
from .forms import BookReviewForm
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
        {
            "book": book,
        },
    )

def author_bio(request, slug_author):
    """
    Displays an individual :model:'horde.Author'.

    **Context**
    ''author''
        An instance of :model:'horde.Author'.
    
    **Template**

    :template: 'horde/author_bio.html
    """

    queryset = Author.objects.all()
    author = get_object_or_404(queryset, slug_author=slug_author)

    return render(
        request,
        "horde/author_bio.html",
        {"author": author},
    )

def new_review(request):

    """
    Takes the data from the book_review_form and saves it to the database
    
    """

    # if request.method == "POST":
    #     n_review = BookReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()

    book_review_form = BookReviewForm()
    if request.method == "POST":
        book_review_form = BookReviewForm(data=request.POST)
    if book_review_form.is_valid():
        book_review_form.save()
    
    
    

    return render(
        request,
        "horde/new_review.html",
        {
           "book_review_form": book_review_form 
        },
    )