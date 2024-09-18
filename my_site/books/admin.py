from django.contrib import admin
from .models import Books, Comment_books
# Register your models here.

admin.site.register(Books)
admin.site.register(Comment_books)
