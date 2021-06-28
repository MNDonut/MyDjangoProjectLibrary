from django.urls import path
from . import views

urlpatterns = [
    path('', views.listOfBooks, name='list'),
    path('book/<int:id>', views.getBookById, name='getBookById')
]