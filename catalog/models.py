from uuid import uuid4
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
# Genre:Models


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)",
    )

    def __str__(self):
        return self.name


# Author:Models
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.id)])

    class Meta:
        ordering = ["last_name", "first_name"]


# Book:Models
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True
    )  # Join with Author model
    summary = models.TextField(
        max_length=1000, help_text="Enter a brief description of the book"
    )
    isbn = models.CharField(
        "ISBN",
        max_length=13,
        help_text="13 Character <a href='https://www.isbn-international.org/content/what-isbn'>ISBN number</a>",
    )
    genre = models.ManyToManyField("Genre", help_text="Select a genre for this book")
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True)

    def display_genre(self):
        return ", ".join(genre.name for genre in self.genre.all()[:3])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])

    class Meta:
        ordering = ["title"]


# BookInstance:Models
class BookInstance(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        help_text="Unique ID for this particular book across whole library",
    )
    book = models.ForeignKey("Book", on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On loan"),
        ("a", "Available"),
        ("r", "Reserved"),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="m",
        help_text="Book availability",
    )

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return f"{self.id} ({self.book.title})"


# Language:Models
class Language(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)",
    )

    def __str__(self):
        return self.name
