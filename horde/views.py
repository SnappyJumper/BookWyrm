from django.db import models
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from .models import Book, Author
from .forms import BookReviewForm, AuthorForm

# Create your views here.

def custom_404(request, exception):
    """
    404 Page View
    """
    # Render the 404.html template
    return render(request, "horde/404.html", {}, status=404)

class BookList(generic.ListView):
    """
    Class based view for the reviews page
    """
    template_name = "horde/reviews.html" # Fetches the template
    paginate_by = 6 # Sets the paginate value so that six reviews display on one page

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
    """
    Class based view for the authors page
    """
    template_name = "horde/authors.html" # Fetches the template
    paginate_by = 6 # Sets the paginate value so that six authors display on one page

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
    """
    Class based view for the Home page
    """
    queryset = Book.objects.filter(status=1)  # Define the queryset
    template_name = "horde/index.html" # Fetches the template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # displays 3 published reviews on the home page
        context["featured_books"] = Book.objects.filter(status=1)[:3]
        # displays 4 published authors on the home page
        context["featured_authors"] = Author.objects.filter(status=1)[:4] 
        return context



def book_review(request, slug):
    """
    Displays an individual review :model:'horde.Book'.
    """
    # Fetches the object from the Book model using the slug value to identify it
    book = get_object_or_404(Book, slug=slug) 

    return render(
        request,
        "horde/book_review.html",
        {"book": book},  # Pass the book to the template
    )

def author_bio(request, slug_author):
    """
    Displays an individual :model:'horde.Author'.
    """
    # Fetches the object from the Author model using the slug_author value to identify it
    author = get_object_or_404(Author, slug_author=slug_author)

    return render(
        request,
        "horde/author_bio.html",
        {"author": author}, # Pass the author to the template
    )

class AddReview(View):
    """
    Class based view for adding reviews to the Book Model
    """
    template_name = "horde/new_review.html" # Fetches the template 

    def get(self, request, *args, **kwargs):
        """
        Fetches the Book Review form and passes it to the template
        """
        form = BookReviewForm()
        return render(request, self.template_name, {"form": form}) # Passes form to the template

    def post(self, request, *args, **kwargs):
        """
        Posts the inputted data to the Review Model
        """
        form = BookReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False) # Prevents the now saved form from committing
            review.review_author = request.user  # Set the logged-in user as the review_author
            review.save() # Saved form is then allowed to commit
            return redirect(reverse("reviews")) 
        return render(request, self.template_name, {"form": form})

def book_edit(request, slug):
    """
    view for editing book reviews
    """
    book = get_object_or_404(Book, slug=slug) # Book instance is retrieved based on the slug value

    # If an unauthorised user attempts to navigate directly to the book edit url they are redirected home
    if request.user != book.review_author:
        messages.error(request, "You are not authorized to edit this Book.")
        return redirect("home")

    # If the edit is posted then the book is updated otherwise it is left untouched
    if request.method == "POST":
        form = BookReviewForm(request.POST, instance=book) # sets the form content to that of the book instance
        if form.is_valid():
            form.save()
            return redirect("book_review", slug=book.slug)
    else:
        form = BookReviewForm(instance=book)

    # Passes the form to the template
    return render(request, "horde/edit_review.html", {"form": form, "book": book})   

def book_delete(request, slug):
    """
    View for deleting a book review
    """
    book = get_object_or_404(Book, slug=slug) # Book instance is retrieved based on the slug value

    # If the User is the owner of the book review then the book is deleted otherwise they are redirected back to reviews
    if book.review_author == request.user:
        book.delete()

    return redirect("reviews")

class AddAuthor(View):
    """
    Class based view for adding an Author to the Author Model
    """
    template_name = "horde/new_author.html" # Fetches the template

    def get(self, request, *args, **kwargs):
        """ 
        Fetches the Author Form and passes it to the template
        """
        form = AuthorForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        """
        Posts the inputted data to the Author model
        """
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False) # Prevents the now saved form from committing
            author.posted_by = request.user # Set logged in User as the posted_by
            form.save() # Saved form is then allowed to commit
            return redirect(reverse("authors"))
        return render(request, self.template_name, {"form": form})

   
def author_edit(request, slug_author):
    """
    view for editing author bios
    """
    author = get_object_or_404(Author, slug_author=slug_author)

    # If an unauthorised user attempts to navigate directly to the edit author url they are redirected home
    if request.user != author.posted_by:
        messages.error(request, "You are not authorized to edit this author.")
        return redirect("home")

    # If the edit is posted then the author is updated otherwise it is left untouched
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author) # sets the form content to that of the author instance
        if form.is_valid():
            form.save()
            messages.success(request, "Author updated successfully.")
            return redirect("author_bio", slug_author=author.slug_author)

    else:
        form = AuthorForm(instance=author)

    # Passes the form to the template
    return render(request, "horde/edit_author.html", {"form": form, "author": author})

def author_delete(request, slug_author):
    """
    view for deleting author bios
    """

    author = get_object_or_404(Author, slug_author=slug_author) # Author instance is retrieved based on the slug value

    # If the User is the owner of the Author Bio then it is deleted otherwise they are redirected back to authors
    if author.posted_by == request.user:
        author.delete()
        messages.add_message(request, messages.SUCCESS, "Author Deleted!")


    return redirect("authors")

