from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage

from .models import Book


NUM_PER_PAGE = 10


def books(request):
    books = Book.objects.all()
    paginator = Paginator(books, NUM_PER_PAGE)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        books = paginator.page(page)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'books/books.html',
                  {'books': books})
