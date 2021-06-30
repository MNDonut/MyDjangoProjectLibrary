import django_filters
from .models import Book, Genre

class BookFilter(django_filters.FilterSet):
    name = django_filters.CharFilter()

    class Meta:
        model = Book
        fields = ['title', 'price', 'genre']