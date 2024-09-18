from django.urls import path
from . import views

urlpatterns = [
    path('', views.films_home, name='films_home'),
    #path('create', views.create, name='create'),
    path('<slug>', views.FilmDetailView.as_view(), name='films-detail'),
    #path('<int:pk>/update', views.SerialsUpdateView.as_view(), name='serial-update'),
    #path('<int:pk>/delete', views.SerialsDeleteView.as_view(), name='serial-delete')
]