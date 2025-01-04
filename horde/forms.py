from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Book, Author
from django import forms

class BookReviewForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ['review_author']  # Exclude review_author from the form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        
        

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

