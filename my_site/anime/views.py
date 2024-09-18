from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CommentAnimeForm
from .models import Anime, Comment_anime
from django.views.generic import DetailView, UpdateView, DeleteView


def anime_home(request):
    anime = Anime.objects.order_by('title')
    return render(request, 'anime/anime_home2.html', {'anime': anime})


class AnimeDetailView(DetailView):
    # model = Anime
    # template_name = 'anime/details_view_anime2.html'
    # context_object_name = 'anime'

    def get(self, request, slug, *args, **kwargs):
        anime = get_object_or_404(Anime, url=slug)
        comment_form = CommentAnimeForm()
        return render(request, 'anime/details_view_anime2.html', context={
            'anime': anime,
            'comment_form': comment_form
        })

    def post(self, request, slug, *args, **kwargs):
        comment_form = CommentAnimeForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['text']
            username = self.request.user
            anime = get_object_or_404(Anime, url=slug)
            comment = Comment_anime.objects.create(anime=anime, username=username, text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/anime'))
        return render(request, 'serials/details_view_anime2.html', context={
            'comment_form': comment_form
        })
