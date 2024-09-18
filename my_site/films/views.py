from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CommentFilmForm
from .models import Films, Comment_film
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.


def films_home(request):
    film = Films.objects.order_by('title')
    return render(request, 'films/films_home2.html', {'film': film})


class FilmDetailView(DetailView):
    # model = Films
    # template_name = 'films/details_view_film2.html'
    # context_object_name = 'film'

    def get(self, request, slug, *args, **kwargs):
        film = get_object_or_404(Films, url=slug)
        comment_form = CommentFilmForm()
        return render(request, 'films/details_view_film2.html', context={
            'film': film,
            'comment_form': comment_form
        })

    def post(self, request, slug, *args, **kwargs):
        comment_form = CommentFilmForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['text']
            username = self.request.user
            film = get_object_or_404(Films, url=slug)
            comment = Comment_film.objects.create(film=film, username=username, text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/serials'))
        return render(request, 'serials/details_view_serial2.html', context={
            'comment_form': comment_form
        })

