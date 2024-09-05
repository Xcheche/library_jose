from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("book/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("create/", views.CreateBook.as_view(), name="create_book"),
]
