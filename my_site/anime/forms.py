from django.forms import ModelForm, Textarea

from .models import Comment_anime


class CommentAnimeForm(ModelForm):

    class Meta:
        model = Comment_anime
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }
