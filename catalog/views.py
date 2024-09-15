from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .models import Book, Author, BookInstance, Genre, Language
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# @login_required
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()
    books = Book.objects.order_by("-id")

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "books": books,
    }

    return render(request, "catalog/index.html", context=context)


# Detail view
class BookDetailView(DetailView):
    model = Book
    template_name = "catalog/book_detail.html"

    def get_context_data(self, **kwargs):
        # Get the default context data from the parent class
        context = super().get_context_data(**kwargs)

        # Add the additional context data you want to include
        context["num_books"] = Book.objects.all().count()
        context["num_instances"] = BookInstance.objects.all().count()
        context["num_instances_available"] = BookInstance.objects.filter(
            status__exact="a"
        ).count()

        return context


# Create View

class CreateBook(LoginRequiredMixin,CreateView):
    model = Book
    fields = "__all__"
    template_name = "catalog/book_form.html"
    success_url = reverse_lazy("index")
