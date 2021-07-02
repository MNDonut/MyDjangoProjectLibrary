from django.urls import path
from . import views

urlpatterns = [
    path('', views.favorite, name='favorite'),
    path('add/<int:id>/', views.add, name='add_or_remove'),
]