from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.


class Serials(models.Model):
    url = models.SlugField()
    title = models.CharField('Название', max_length=51)
    genre = models.CharField('Жанр', max_length=51)
    release_date = models.DateField('Дата выхода')
    director = models.CharField('Режиссер', max_length=51)
    age = models.CharField('Возраст', max_length=51)
    avg_time = models.CharField('Среднее время серии', max_length=51)
    in_roles = models.CharField('В ролях', max_length=250)
    description = models.TextField('Про сериал')
    poster = models.ImageField('Постер сериала', upload_to='serials/')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return f'/serials/{self.id}'

    class Meta:
        verbose_name = 'Сериал'
        verbose_name_plural = 'Сериалы'


class Comment_serial(models.Model):
    serial = models.ForeignKey(Serials, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name_serial')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.text
