from .models import Book, Author
from django import forms

class BookReviewForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ["review_author"]  # Exclude review_author from the form

        widgets = {
            "book_published": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }
    
        
        

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        exclude = ["posted_by"]

        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }
