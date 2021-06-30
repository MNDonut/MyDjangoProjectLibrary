from django.db.models import fields
import django_filters
from .models import Book

# django-filter automatically define what type of filters need to use
# for separate field or you can redefine it(like price below)

class BookFilter(django_filters.FilterSet):

    # don't use it because of '-' between two price inputs
    # price = django_filters.RangeFilter(label='Price between')
    # lookup_expr shows django a comparable symbol
    price__gte = django_filters.NumberFilter(field_name='price', label='Price from', lookup_expr='gte')
    price__lte = django_filters.NumberFilter(field_name='price', label='Price up to', lookup_expr='lte')
    o = django_filters.OrderingFilter(fields=(
        'title', 'price'
    ))

    class Meta:
        model = Book
        fields = ['title', 'genre', 'language']

class BookFilterWithoutGenre(django_filters.FilterSet):
    o = django_filters.OrderingFilter(fields=(
        'title', 'price'
    ))
    price__gte = django_filters.NumberFilter(field_name='price', label='Price from', lookup_expr='gte')
    price__lte = django_filters.NumberFilter(field_name='price', label='Price up to', lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['title', 'language']