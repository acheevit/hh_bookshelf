from django.shortcuts import render

from .models import Book


def books(request):
    return render(request, 'books/books.html',
                  {'books': Book.objects.all()})
