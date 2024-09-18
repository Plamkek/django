from django.urls import path
from . import views

urlpatterns = [
    path('', views.anime_home, name='anime_home'),
    path('<slug>', views.AnimeDetailView.as_view(), name='anime-detail'),
]
