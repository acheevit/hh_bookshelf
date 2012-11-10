#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import template


register = template.Library()


@register.inclusion_tag('books/includes/show_authors.html')
def show_authors(book):
    return {'authors': book.authors.all()}
