from django.urls import path
from . import views

urlpatterns = [
    path('', views.listOfBooks, name='list'),
    path('book/<slug:slug>/', views.getBookByName, name='getBookByName'),
    path('category/<str:category>/', views.getBooksByCategory, name='getBooksByCategory'),
]