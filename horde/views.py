from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
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
    Displays an individual review :model:'horde.Book'.
    """
    queryset = Book.objects.filter(status=1)  # Fetch only published reviews
    book = get_object_or_404(queryset, slug=slug)

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

      

class AddAuthor(View):

    template_name = "horde/new_author.html"

    def get(self, request, *args, **kwargs):
        form = AuthorForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("authors"))
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
