from django.contrib import messages
from django.db import models
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from .models import Book, Author
from .forms import BookReviewForm, AuthorForm

# Create your views here.


def custom_404(request, exception):
    """
    Renders the 404 Page View
    """
    # Render the 404.html template
    return render(request, "horde/404.html", {}, status=404)


class BookList(generic.ListView):
    """
    Renders the most recent information from the Book Model and allows
    authenticated users to enter them
    Displays multiple instances of :model:`horde.Book`
    **Context**
    ``horde``
    Instances aranged by title of :model:`horde.Book`
    **Template**
    :template:`horde/reviews.html`
    """
    template_name = "horde/reviews.html"  # Fetches the template
    # Sets the paginate value so that six reviews display on one page
    paginate_by = 6

    def get_queryset(self):
        """
        Fetches the queryset
        """
        # determines if the logged in user making the request is
        # properly authenticated
        if self.request.user.is_authenticated:
            # Show published reviews to all users and
            # drafts only to the user who made them
            return Book.objects.filter(
                models.Q(status=1) | models.Q(status=0,
                                              review_author=self.request.user)
            )
        else:
            # Users who are not logged in can only see published reviews
            return Book.objects.filter(status=1)


class AuthorList(generic.ListView):
    """
    Renders the most recent information from the Author Model and allows
    authenticated users to enter them
    Displays multiple instances of :model:`horde.Author`
    **Context**
    ``horde``
    Instances aranged by name of :model:`horde.Author`
    **Template**
    :template:`horde/authors.html`
    """
    template_name = "horde/authors.html"  # Fetches the template
    # Sets the paginate value so that six authors display on one page
    paginate_by = 6

    def get_queryset(self):
        """
        Fetches the queryset
        """
        # determines if the logged in user making the request is
        # properly authenticated
        if self.request.user.is_authenticated:
            # Show published Author Bios to all users and
            # drafts to only the user who made them
            return Author.objects.filter(
                models.Q(status=1) | models.Q(status=0,
                                              posted_by=self.request.user)
            )
        else:
            # Users who are not logged in can only see published Author Bios
            return Author.objects.filter(status=1)


class HomeBookList(generic.ListView):
    """
    Renders the most recent information from the Book Model and
    Author Model and allows
    authenticated users to enter them
    Displays three instances of :model:`horde.Book`
    Displays four instances of :model:`horde.Author`
    **Context**
    ``horde``
    Three instances aranged by title of :model:`horde.Book`
    Four instances arranged by name of :model:`horde.Author`
    **Template**
    :template:`horde/index.html`
    """
    queryset = Book.objects.filter(status=1)  # Define the queryset
    template_name = "horde/index.html"  # Fetches the template

    def get_context_data(self, **kwargs):
        """
        Fetches the data from the database
        """
        context = super().get_context_data(**kwargs)
        # displays 3 published reviews on the home page
        context["featured_books"] = Book.objects.filter(status=1)[:3]
        # displays 4 published authors on the home page
        context["featured_authors"] = Author.objects.filter(status=1)[:4]
        return context


def book_review(request, slug):
    """
    Renders the most recent information from the Book Model and allows
    user collaboration requests
    Displays an individual instance of :model:`horde.Book`
    **Context**
    ``horde``
    Calls an individual instance of :model:`horde.Book`
    **Template**
    :template:`horde/book-review.html`
    """
    # Fetches the object from the Book model using the slug value
    # to identify it
    book = get_object_or_404(Book, slug=slug)

    if book.status == 0 and book.review_author != request.user:
        messages.error(request, "You are not authorized to view this draft.")
        return redirect("home")  # Redirect unauthorized users to the home page

    return render(
        request,
        "horde/book_review.html",
        {"book": book},  # Pass the book to the template
    )


def author_bio(request, slug_author):
    """
    Renders the most recent information from the Author Model and allows
    user collaboration requests
    Displays an individual instance of :model:`horde.Author`
    **Context**
    ``horde``
    Calls an individual instance of :model:`horde.Author`
    **Template**
    :template:`horde/author-bio.html`
    """
    # Fetches the object from the Author model using the slug_author
    # value to identify it
    author = get_object_or_404(Author, slug_author=slug_author)

    # Check if the author bio is a draft and if the user is not the creator
    if author.status == 0 and author.posted_by != request.user:
        messages.error(request, "You are not authorized to view this draft.")
        return redirect("home")  # Redirect unauthorized users to the home page

    return render(
        request,
        "horde/author_bio.html",
        {"author": author},  # Pass the author to the template
    )


class AddReview(View):
    """
    Renders the form BookReviewForm and allows user collaboration
    requests
    Adds an individual entry to :model:`horde.Book`
    Uses :model:`horde.Author` to do this
    **Context**
    ``horde``
    Creates an individual instance of :model:`horde.Book`
    Calls the form BookReviewForm
    User selects an author from the :model:`horde.Author` in the
    form
    **Template**
    :template:`horde/new-review.html`
    """
    template_name = "horde/new_review.html"  # Fetches the template

    def get(self, request, *args, **kwargs):
        """
        Fetches the Book Review form and passes it to the template
        """
        if not request.user.is_authenticated:
            # Add a message before redirecting
            messages.error(request,
                           "You must be logged in to alter content.")
            return redirect("account_login")  # Redirects to login

        form = BookReviewForm()
        # Passes form to the template
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        """
        Posts the inputted data to the Review Model
        """
        if not request.user.is_authenticated:
            # Add a message before redirecting
            messages.error(request, "You must be logged in to alter content.")
            return redirect("account_login")  # Redirects to login

        form = BookReviewForm(request.POST)
        if form.is_valid():
            # Prevents the now saved form from committing
            review = form.save(commit=False)
            # Set the logged-in user as the review_author
            review.review_author = request.user
            review.save()  # Saved form is then allowed to commit
            messages.success(request, "Review added successfully.")
            return redirect(reverse("reviews"))
        return render(request, self.template_name, {"form": form})


def book_edit(request, slug):
    """
    Renders the form BookReviewForm for the specified slug value
    fills it with the relevent content from :model:`horde.Book`
    and allows user collaboration requests
    Edits an individual entry to :model:`horde.Book`
    Calls an instance from :model:`horde.Author`
    **Context**
    ``horde``
    Pulls an individual instance of :model:`horde.Book`
    Calls the form BookReviewForm and populates it with the data
    Calls the :model:`horde.Author` if the user wants to change authors
    Posts the edited version back to :model:`horde.Book`
    **Template**
    :template:`horde/edit-review.html`
    """
    # Book instance is retrieved based on the slug value
    book = get_object_or_404(Book, slug=slug)

    # If an unauthorised user attempts to navigate directly to
    # the book edit url they are redirected
    if request.user != book.review_author:
        messages.error(request, "You are not authorized to edit this content.")
        return redirect("home")

    # If the edit is posted then the book is updated otherwise
    # it is left untouched
    if request.method == "POST":
        # sets the form content to that of the book instance
        form = BookReviewForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated successfully.")
            return redirect("book_review", slug=book.slug)
    else:
        form = BookReviewForm(instance=book)

    # Passes the form to the template
    return render(request, "horde/edit_review.html",
                  {"form": form, "book": book})


def book_delete(request, slug):
    """
    Deletes a specified review from the Book Model
    Removes an individual entry based on the slug value from
    :model:`horde.Book`
    **Context**
    ``horde``
    Calls the individual instance from the :model:`horde.Book`
    **Template**
    none
    """
    # Book instance is retrieved based on the slug value
    book = get_object_or_404(Book, slug=slug)
    # If the User is the owner of the book review then
    # the book is deleted otherwise they are redirected back to reviews
    if book.review_author == request.user:
        book.delete()
        messages.success(request, "Review successfully Deleted!")
    else:
        # Add a message before redirecting
        messages.error(request,
                       "You are not authorised to delete this content.")
    return redirect("reviews")


class AddAuthor(View):
    """
    Renders the form AuthorForm and allows user collaboration
    requests
    Adds an individual entry to :model:`horde.Author`
    **Context**
    ``horde``
    Creates an individual instance of :model:`horde.Author`
    Calls the form AuthorForm
    **Template**
    :template:`horde/new-author.html`
    """
    template_name = "horde/new_author.html"  # Fetches the template

    def get(self, request, *args, **kwargs):
        """
        Fetches the Author Form and passes it to the template
        """
        if not request.user.is_authenticated:
            # Add a message before redirecting
            messages.error(request, "You must be logged in to alter content.")
            return redirect("account_login")  # Redirects to login

        form = AuthorForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        """
        Posts the inputted data to the Author model
        """
        if not request.user.is_authenticated:
            # Add a message before redirecting
            messages.error(request, "You must be logged in to alter content.")
            return redirect("account_login")  # Redirects to login

        form = AuthorForm(request.POST)
        if form.is_valid():
            # Prevents the now saved form from committing
            author = form.save(commit=False)
            # Set logged in User as the posted_by
            author.posted_by = request.user
            form.save()  # Saved form is then allowed to commit
            messages.success(request, "Author added successfully.")
            return redirect(reverse("authors"))
        return render(request, self.template_name, {"form": form})


def author_edit(request, slug_author):
    """
    Renders the form AuthorForm for the specified slug_author
    value, fills it with the relevent content from :model:`horde.Author`
    and allows user collaboration requests
    Edits an individual entry to :model:`horde.Author`
    **Context**
    ``horde``
    Pulls an individual instance of :model:`horde.Author`
    Calls the form BookReviewForm and populates it with the data
    Posts the edited version back to :model:`horde.Author`
    **Template**
    :template:`horde/edit-author.html`
    """
    author = get_object_or_404(Author, slug_author=slug_author)

    # If an unauthorised user attempts to navigate directly
    # to the edit author url they are redirected home
    if request.user != author.posted_by:
        messages.error(request, "You are not authorized to edit this author.")
        return redirect("home")

    # If the edit is posted then the author is updated otherwise
    # it is left untouched
    if request.method == "POST":
        # sets the form content to that of the author instance
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, "Author updated successfully.")
            return redirect("author_bio", slug_author=author.slug_author)

    else:
        form = AuthorForm(instance=author)

    # Passes the form to the template
    return render(request, "horde/edit_author.html",
                  {"form": form, "author": author})


def author_delete(request, slug_author):
    """
    Deletes a specified author from the Author Model
    Removes an individual entry based on the slug_author value from
    :model:`horde.Author`
    **Context**
    ``horde``
    Calls the individual instance from the :model:`horde.Author`
    **Template**
    none
    """
    # Author instance is retrieved based on the slug value
    author = get_object_or_404(Author, slug_author=slug_author)

    # If the User is the owner of the Author Bio then it is
    # deleted otherwise they are redirected back to authors
    if author.posted_by == request.user:
        author.delete()
        messages.success(request, "Author successfully Deleted!")
    else:
        # Add a message before redirecting
        messages.error(request,
                       "You are not authorised to delete this content.")

    return redirect("authors")
