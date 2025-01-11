from django.db import models
from django.contrib.auth.models import User

STAR = ((0, "1-5"), (1, "One Star"), (2, "Two Star"), (3, "Three Star"),
        (4, "Four Star"), (5, "Five Star"))
STATUS = ((0, "Save as Draft"), (1, "Post"))

# Create your models here.


class Author(models.Model):
    """
    Stores a single Author entry related to :model:`auth.User`
    """
    name = models.CharField(max_length=100, unique=True)
    # slug_author value is used to help identify individual Author instances
    slug_author = models.SlugField(max_length=100, unique=True)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    favourite_book = models.CharField(max_length=200)
    bio = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    # Foreign Key which links the Author Model to the User
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name="author_bios")

    class Meta:
        """
        Organises the data in the Author Model
        """
        ordering = ["name"]  # arranges data by name alphabetically

    def __str__(self):
        """
        Returns name as the Author instance's heading
        """
        return f"{self.name}"


class Book(models.Model):
    """
    Stores a single Author entry related to :model:`auth.User`
    and :model:`horde.Author`
    """
    title = models.CharField(max_length=200, unique=True)
    # slug value is used to help identify individual Book instances
    slug = models.SlugField(max_length=200, unique=True)
    # Foreign key which links the Book Model to the Author Model
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    genre = models.CharField(max_length=50)
    book_published = models.DateField()
    review = models.TextField()
    rating = models.IntegerField(choices=STAR, default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    # Foreign Key which links the Book Model to the User
    review_author = models.ForeignKey(User, on_delete=models.CASCADE,
                                      related_name="book_reviews")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Organises the data in the Book Model
        """
        ordering = ["title"]  # arranges data by title alphabetically

    def __str__(self):
        """
        Returns title as the Book instance's heading
        """
        return f"Title: {self.title}"
