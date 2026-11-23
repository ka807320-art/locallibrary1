from django.shortcuts import get_object_or_404, render
from .models import Book, Author, Language


def home(request):
    return render(request, "catalog/home.html", {
        "book_count": Book.objects.count(),
        "author_count": Author.objects.count(),
        "language_count": Language.objects.count(),
    })


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "catalog/book_detail.html", {"book": book})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, "catalog/author_detail.html", {"author": author})


def language_detail(request, pk):
    language = get_object_or_404(Language, pk=pk)
    return render(request, "catalog/language_detail.html", {"language": language})
