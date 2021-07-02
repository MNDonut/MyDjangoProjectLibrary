from django.shortcuts import redirect, render
from .models import Mark
from book.models import Book
from django.http import HttpResponseRedirect

def favorite(request):
    marks = Mark.objects.filter(user__email=request.user.email)
    return render(request, 'favorite.html', {'list': marks})

def add(request, id):
    book = Book.objects.get(pk=id)
    # firstly i check is this book alredy marked
    # if it's marked i change bookmark and delete from favorite 
    isMarked = Mark.objects.filter(user=request.user, book=book)
    if isMarked:
        isMarked.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    isMarked = Mark.objects.create(user=request.user, book=book)
    isMarked.save()
    # redirect to the same page
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))