# Generated by Django 4.2.5 on 2023-10-31 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.SlugField()),
                ('title', models.CharField(max_length=51, verbose_name='Название')),
                ('genre', models.CharField(max_length=51, verbose_name='Жанр')),
                ('release_date', models.CharField(max_length=51, verbose_name='Дата выхода')),
                ('author', models.CharField(max_length=51, verbose_name='Автор')),
                ('pages', models.CharField(max_length=51, verbose_name='Количество страниц')),
                ('description', models.TextField(verbose_name='Про книгу')),
                ('poster', models.ImageField(upload_to='books/', verbose_name='Постер книги')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]