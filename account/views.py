from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, CustomLoginForm

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

def home(request):
    return render(request, 'common/base.html')