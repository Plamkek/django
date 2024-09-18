from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.


class Anime(models.Model):
    url = models.SlugField()
    title = models.CharField('Название', max_length=51)
    genre = models.CharField('Жанр', max_length=51)
    release_date = models.DateField('Дата выхода')
    age = models.CharField('Возраст', max_length=51)
    avg_time = models.CharField('Среднее время серии', max_length=51)
    description = models.TextField('Про аниме')
    poster = models.ImageField('Постер аниме', upload_to='anime/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/anime/{self.id}'

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'


class Comment_anime(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name_anime')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text