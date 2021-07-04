from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Book
from .filters import BookFilter, BookFilterWithoutGenre
from bookmark.models import Mark

def listOfBooks(request):
    books = Book.objects.all()
    filter = BookFilter(request.GET, queryset=books)
    return render(request, 'all_books.html', {'books': books, 'filter': filter})

def getBookByName(request, slug):
    # render book page
    # also check is current book marked and change bookmark button
    currentBook = Book.objects.get(slug=slug)
    book = Book.objects.get(slug=slug)
    # i don't allow users to save books if they aren't authenticated
    if request.user.is_authenticated:
        isItMarkedBook = Mark.objects.filter(user=request.user, book=currentBook)
        if isItMarkedBook:
            saved = True
            return render(request, 'book_page.html', {'book': book, 'saved': saved})
    saved = False
    return render(request, 'book_page.html', {'book': book, 'saved': saved})
        

def getBooksByCategory(request, category):
    # genre__genre - class__field
    # not genre=category cuz it's a foreign key
    allBooks = Book.objects.filter(genre__genre=category)
    filter = BookFilterWithoutGenre(request.GET, queryset=allBooks)
    return render(request, 'category_books.html', {'category': category, 'allBooks': allBooks, 'filter': filter})