from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Book, Author
from .forms import BookReviewForm, AuthorForm
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

def new_author(request):
    """
    Creates an instance of the AuthorForm, saves it to the variable author_form and saves it to the database
    """

    author_form = AuthorForm()
    if request.method == "POST":
        author_form = AuthorForm(data=request.POST)
    if author_form.is_valid():

        author_form.save()

    return render(
        request,
        "horde/new_author.html",
        {
            "author_form": author_form
        }
    )

def book_edit(request, slug):
    """
    view for editing book reviews
    """
    # if request.method == "POST":
    #     queryset = Book.objects.filter(status=1)
    #     book = get_object_or_404(queryset, slug=slug)
    #     book_content =get_object_or_404(Book, pk=book_id) 
    #     edit_book_review_form = BookReviewForm(data=request.POST, instance= book)

    #     if edit_book_review_form.is_valid() and comment.author == request.user:
    #         book = edit_book_review_form.save()
    #         messages.add_message(request, messages.SUCCESS, "Review Updated!")
    #     else:
    #         messages.add_message(request, messages.ERROR, "Error updating Review!")

    # return HttpResponseRedirect(reverse("book_review", args=[slug]))
    queryset = Book.objects.filter(status=1)
    book = get_object_or_404(queryset, slug=slug)
    edit_book_review_form = BookReviewForm(request.POST, instance=book)
    
    if request.method == "POST":
        
        if edit_book_review_form.is_valid and book.review_author == request.user:
            edit_book_review_form.save()
    
    return render(
        request,
        "horde/edit_review.html",
        {
           "edit_book_review_form": edit_book_review_form 
        },
    )