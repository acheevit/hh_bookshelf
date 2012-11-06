# -*- coding: utf-8 -*-

import os
import json

from django.core.management.base import BaseCommand

FILE = os.path.join(os.path.dirname(
                    os.path.abspath(__file__)),
                    'books'
                    )


from bookstore.books.models import Book, Author


class Command(BaseCommand):
    args = ''
    help = 'Load books'

    def handle(self, *args, **options):

        # clean first
        Book.objects.all().delete()
        Author.objects.all().delete()

        lines = []
        with open(FILE, 'r') as f:
            lines = f.readlines()

        for i in range(0, len(lines), 3):
            title = lines[i].replace('\n', '')
            author = lines[i+1].replace('\n', '')[3:].split(',')[0]
            price = lines[i+2].replace('\n', '')[8:]

            au = Author()
            au.name = author
            au.save()
            book = Book()
            book.author = au
            book.title = title
            book.price = price
            book.save()
