from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from book.models import Book

class Mark(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    book = models.ForeignKey(Book, on_delete=CASCADE)

    def __str__(self):
        return str(self.book)
