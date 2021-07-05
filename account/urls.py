from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
from .forms import CustomLoginForm
# using built-in django login & logout views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    # using custom form for adding placeholders
    path('login/', auth_view.LoginView.as_view(template_name='login.html', authentication_form=CustomLoginForm), name='login')
]