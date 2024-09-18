from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.


class Films(models.Model):
    url = models.SlugField()
    title = models.CharField('Название', max_length=51)
    genre = models.CharField('Жанр', max_length=51)
    release_date = models.DateField('Дата выхода')
    director = models.CharField('Режиссер', max_length=51)
    age = models.CharField('Возраст', max_length=51)
    time = models.CharField('Время', max_length=51)
    in_roles = models.CharField('В ролях', max_length=250)
    description = models.TextField('Про фильм')
    poster = models.ImageField('Постер фильма', upload_to='films/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/films/{self.id}'

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Comment_film(models.Model):
    film = models.ForeignKey(Films, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name_film')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text