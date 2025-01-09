from .models import Book, Author
from django_summernote.widgets import SummernoteWidget
from django import forms

class BookReviewForm(forms.ModelForm):
    """
    The form class for the Book Model
    """
    class Meta:
        model = Book # Sets the model to Book
        fields = "__all__" # Retrieves all the fields from Book
        exclude = ["review_author"]  # Exclude review_author from the form

        widgets = {
            # Applies additional properties to each field when displayed 
            # Changes the book_published input to a Date Input and applies the form-control class to it
            "book_published": forms.DateInput(attrs={"type": "date", "class": "form-control"}), 
            "review": SummernoteWidget(), # Allows the user to create rich text content for the review field
        }
    
        
        

class AuthorForm(forms.ModelForm):
    """ 
    The form class for the Author Model
    """
    class Meta:
        model = Author # Sets the model to Author
        fields = "__all__" # Retrieves all the fields from Author
        exclude = ["posted_by"] # Excludes posted_by from the form

        widgets = {
            # Applies additional properties to each field when displayed
            # Changes the date_of_birth input to a Date Input and applies the form-control class to it
            "date_of_birth": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "bio": SummernoteWidget(), # Allows the user to create rich text content for the bio field
        }
