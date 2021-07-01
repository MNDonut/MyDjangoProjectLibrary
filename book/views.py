from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Book
from .filters import BookFilter, BookFilterWithoutGenre

def listOfBooks(request):
    books = Book.objects.all()
    filter = BookFilter(request.GET, queryset=books)
    return render(request, 'all_books.html', {'books': books, 'filter': filter})

def getBookByName(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'book_page.html', {'book': book})

def getBooksByCategory(request, category):
    # genre__genre - class__field
    # not genre=category cuz it's a foreign key
    allBooks = Book.objects.filter(genre__genre=category)
    filter = BookFilterWithoutGenre(request.GET, queryset=allBooks)
    return render(request, 'category_books.html', {'category': category, 'allBooks': allBooks, 'filter': filter})