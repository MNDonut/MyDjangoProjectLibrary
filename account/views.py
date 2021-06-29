from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from book import models as BookModels

def home(request):
    genres = BookModels.Genre.objects.all()
    booksToShow = dict()
    for genre in genres:
        randomBooksInThisGenre = BookModels.Book.objects.filter(genre=genre).order_by('?')[:5]
        booksToShow[genre] = randomBooksInThisGenre
    return render(request, 'common/home.html', {'context': booksToShow})

# if user'll try to open own account it'll redirect to login page firstly
@login_required
def account(request):
    user = User.objects.get(username=request.user.username)
    return render(request, 'account_page.html', {'currentUser': user})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'register.html', {'form': form})
    form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})