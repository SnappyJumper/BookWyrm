from .models import Book, Author
from django import forms

class BookReviewForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

