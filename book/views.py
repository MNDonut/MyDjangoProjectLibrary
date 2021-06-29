from django.shortcuts import render
from django.http import HttpResponse

def listOfBooks(request):
    pass

def getBookByName(request, slug):
    return HttpResponse('by-slug')

def getBooksByCategory(request, category):
    return HttpResponse('category')