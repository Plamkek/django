from django.forms import ModelForm, Textarea

from .models import Comment_film


class CommentFilmForm(ModelForm):

    class Meta:
        model = Comment_film
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }
