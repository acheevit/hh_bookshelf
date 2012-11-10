from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=64)
    books = models.ManyToManyField('books.Book')


class Book(models.Model):
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
