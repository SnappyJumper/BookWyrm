from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import TemplateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
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

# def new_author(request):
#     """
#     Creates an instance of the AuthorForm, saves it to the variable author_form and saves it to the database
#     """

    # author_form = AuthorForm()
    # if request.method == "POST":
    #     author_form = AuthorForm(data=request.POST)
    # if author_form.is_valid():

    #     author_form.save()

    # return render(
    #     request,
    #     "horde/new_author.html",
    #     {
    #         "author_form": author_form
    #     }
    # )

    # return redirect(reverse("authors"))

class AddAuthor(View):
    template_name = "horde/new_author.html"
    

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "horde/new_author.html",
        )

    def post(self, request):
        
        new_name = request.POST.get("name")
        new_slug_author = request.POST.get("slug_author")
        new_date_of_birth= request.POST.get("date_of_birth")
        new_nationality = request.POST.get("nationality")
        new_genre = request.POST.get("genre")
        new_favourite_book = request.POST.get("favourite_book")
        new_bio = request.POST.get("bio")

        CreateNewAuthor = Author.objects.create(
            name = new_name,
            slug_author = new_slug_author,
            date_of_birth = new_date_of_birth,
            nationality = new_nationality,
            genre = new_genre,
            favourite_book = new_favourite_book,
            bio = new_bio,
        )

        CreateNewAuthor.save()

        return redirect(reverse('authors'))

def book_edit(request, slug):
    """
    view for editing book reviews
    """
    
    queryset = Book.objects.filter(status=1)
    book = get_object_or_404(queryset, slug=slug)
    edit_book_review_form = BookReviewForm(request.POST, instance=book)
    
    if request.method == "POST":
        
        if edit_book_review_form.is_valid and book.review_author == request.user:
            edit_book_review_form.save()
    
    return 
    render
    (
        request,
        "horde/edit_review.html",
        {
           "edit_book_review_form": edit_book_review_form 
        },
     )


def book_delete(request, slug):

    queryset = Book.objects.filter(status=1)
    book = get_object_or_404(queryset, slug=slug)

    if book.review_author == request.user:
        book.delete()
        messages.add_message(request, messages.SUCCESS, "Review Deleted!")
    else:
        messages.add_message(request, messages.ERROR, "You can only delete your own Reviews!")

    return HttpResponseRedirect(reverse("reviews"))
