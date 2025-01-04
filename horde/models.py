from django.db import models
from django.contrib.auth.models import User

STAR = ((0, "1-5"),(1, "One Star"),(2, "Two Star"),(3, "Three Star"),(4, "Four Star"),(5, "Five Star"))
STATUS = ((0, "Save as Draft"),(1, "Post"))

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug_author = models.SlugField(max_length=100, unique=True)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    favourite_book = models.CharField(max_length=200)
    bio = models.TextField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    genre = models.CharField(max_length=50)
    book_published = models.DateField()
    review = models.TextField()
    rating = models.IntegerField(choices=STAR, default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    review_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="book_reviews")
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Title: {self.title}"
    


