from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, CustomLoginForm

@login_required
def account(request):
    if request.method == 'POST':
        return redirect('logout/')
    user = User.objects.get(username=request.user.username)
    return render(request, 'account_page.html', {'currentUser': user})

def register(request):
    loginForm = CustomLoginForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/login', {'form': loginForm})
        else:
            return render(request, 'register.html', {'form': form})
    form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
