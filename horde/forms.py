from .models import Book
from django import forms

class BookReviewForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        # fields = (
        #     "title",
        #     "slug",
        #     "author",
        #     "genre",
        #     "book_published",
        #     "review",
        #     "rating",
        #     "status",
        #     "review_author",
        #     )