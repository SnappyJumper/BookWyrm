from django.db import models
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from .models import Book, Author
from .forms import BookReviewForm, AuthorForm

# Create your views here.

class BookList(generic.ListView):
    template_name = "horde/reviews.html"
    paginate_by = 6

    def get_queryset(self):
        # determines if the logged in user making the request is properly authenticated
        if self.request.user.is_authenticated:
            # Show published reviews to all users and drafts only to the user who made them
            return Book.objects.filter(
                models.Q(status=1) | models.Q(status=0, review_author=self.request.user)
            )
        else:
            # Users who are not logged in can only see published reviews
            return Book.objects.filter(status=1)

class AuthorList(generic.ListView):
    template_name = "horde/authors.html"
    paginate_by = 6 

    def get_queryset(self):
        # determines if the logged in user making the request is properly authenticated
        if self.request.user.is_authenticated:
            # Show published Author Bios to all users and drafts to only the user who made them
            return Author.objects.filter(
                models.Q(status=1) | models.Q(status=0, posted_by=self.request.user)
            )
        else:
            # Users who are not logged in can only see published Author Bios
            return Author.objects.filter(status=1)



class HomeBookList(generic.ListView):
    queryset = Book.objects.all() 
    template_name = "horde/index.html"
    paginate_by = 6  



def book_review(request, slug):
    """
    Displays an individual review :model:'horde.Book'.
    """
    
    book = get_object_or_404(Book, slug=slug)

    if book.status == 0 and book.review_author != request.user:

        messages.error(request, "You are not authorised to view this draft.")
        return redirect("reviews")

    return render(
        request,
        "horde/book_review.html",
        {"book": book},  # Pass the book to the template
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

class AddReview(View):
    
    template_name = "horde/new_review.html"

    def get(self, request, *args, **kwargs):
        form = BookReviewForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = BookReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.review_author = request.user  # Set the logged-in user as the review_author
            review.save()
            return redirect(reverse("reviews"))
        return render(request, self.template_name, {"form": form})

def book_edit(request, slug):
    """
    view for editing book reviews
    """
    book = get_object_or_404(Book, slug=slug)

    if request.user != book.review_author:
        messages.error(request, "You are not authorized to edit this review.")
        return redirect("home")

    if request.method == "POST":
        form = BookReviewForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated successfully.")
            return redirect("book_review", slug=book.slug)
    else:
        form = BookReviewForm(instance=book)

    return render(request, "horde/edit_review.html", {"form": form, "book": book})    

def book_delete(request, slug):

    queryset = Book.objects.filter(status=1)
    book = get_object_or_404(queryset, slug=slug)

    if book.review_author == request.user:
        book.delete()
        messages.add_message(request, messages.SUCCESS, "Review Deleted!")
    else:
        messages.add_message(request, messages.ERROR, "You can only delete your own Reviews!")

    return redirect("reviews")

class AddAuthor(View):
    template_name = "horde/new_author.html"

    def get(self, request, *args, **kwargs):
        form = AuthorForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.posted_by = request.user # Set logged in User as the posted_by
            form.save()
            return redirect(reverse("authors"))
        return render(request, self.template_name, {"form": form})

   
def author_edit(request, slug_author):
    """
    view for editing author bios
    """
    author = get_object_or_404(Author, slug_author=slug_author)

    if request.user != author.posted_by:
        messages.error(request, "You are not authorized to edit this author.")
        return redirect("home")

    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, "Author updated successfully.")
            # return redirect("authors")
            return redirect("author_bio", slug_author=author.slug_author)

    else:
        form = AuthorForm(instance=author)

    return render(request, "horde/edit_author.html", {"form": form, "author": author})

def author_delete(request, slug_author):
    """
    view for deleting author bios
    """

#     queryset = Book.objects.filter(status=1)
#     book = get_object_or_404(queryset, slug=slug)

#     if book.review_author == request.user:
#         book.delete()
#         messages.add_message(request, messages.SUCCESS, "Review Deleted!")
#     else:
#         messages.add_message(request, messages.ERROR, "You can only delete your own Reviews!")

#     return redirect("reviews")
    queryset = Author.objects.all()
    author = get_object_or_404(queryset, slug_author=slug_author)

    if author.posted_by == request.user:
        author.delete()
        messages.add_message(request, messages.SUCCESS, "Author Deleted!")
    else:
        messages.add_message(request, messages.ERROR, "You can only delete your own Authors!")

    return redirect("authors")