from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .filters import BookFilter

def listOfBooks(request):
    books = Book.objects.all()
    return render(request, 'all_books.html', {'books': books})

def getBookByName(request, slug):
    return HttpResponse('by-slug')

def getBooksByCategory(request, category):
    # genre__genre - class__field
    # not genre=category cuz it's a foreign key
    allBooks = Book.objects.filter(genre__genre=category)
    return render(request, 'category_books.html', {'category': category, 'allBooks': allBooks})