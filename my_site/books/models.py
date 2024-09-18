from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.


class Books(models.Model):
    url = models.SlugField()
    title = models.CharField('Название', max_length=51)
    genre = models.CharField('Жанр', max_length=51)
    release_date = models.CharField('Дата выхода', max_length=51)
    author = models.CharField('Автор', max_length=51)
    pages = models.CharField('Количество страниц', max_length=51)
    description = models.TextField('Про книгу')
    poster = models.ImageField('Постер книги', upload_to='books/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/books/{self.id}'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Comment_books(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name_book')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text