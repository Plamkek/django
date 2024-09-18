from .models import Books, Comment_books
from django.forms import ModelForm, TextInput, Textarea, DateField, IntegerField, DateInput


class CommentBookForm(ModelForm):

    class Meta:
        model = Comment_books
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }
class BooksFrom(ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'genre', 'release_date', 'author', 'pages', 'description', 'poster']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название сериала'
            }),
            'genre': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Жанр'
            }),
            'release_date': DateInput(attrs={
                'class': 'form-control',
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Режиссер'
            }),
            'pages': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возрастное ограничение'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            })
        }
