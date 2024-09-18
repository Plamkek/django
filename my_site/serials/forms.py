from .models import Serials
from django.forms import ModelForm, TextInput, Textarea, DateField, IntegerField, DateInput
from .models import Comment_serial


class CommentSerialForm(ModelForm):

    class Meta:
        model = Comment_serial
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }


class SerialsFrom(ModelForm):
    class Meta:
        model = Serials
        fields = ['title', 'genre', 'release_date', 'director', 'age', 'avg_time', 'in_roles', 'description', 'poster']

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
            'director': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Режиссер'
            }),
            'age': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возрастное ограничение'
            }),
            'avg_time': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Среднее время серии(в минутах)'
            }),
            'in_roles': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'В ролях'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            })
        }
