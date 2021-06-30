from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
# pip install django-slugger
# Auto create slug for human-readable url
from slugger import AutoSlugField

def isBiggerThanZero(n):
    if n <= 0:
        raise ValidationError('Price can\'t be less than zero!')

class Book(models.Model):
    LANGUAGES = (
        ('ukr', 'Ukrainian'),
        ('eng', 'English'),
        ('rus', 'Russian'),
    )
    image = models.ImageField(upload_to='images/', default='4.jpg')
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    language = models.CharField(choices=LANGUAGES, default='English', max_length=100)
    # many books has one genre, if genre is deleted then delete related books
    genre = models.ForeignKey('Genre', on_delete=CASCADE)
    price = models.DecimalField(validators=[isBiggerThanZero], max_digits=6, decimal_places=2)
    slug = AutoSlugField(populate_from='title', default='')

    def __str__(self):
        return self.title

class Genre(models.Model):
    genre = models.CharField(max_length=32, default='')

    def __str__(self):
        return self.genre