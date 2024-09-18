from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_home, name='books_home'),
    #path('create', views.create, name='create'),
    path('<slug>', views.BooksDetailView.as_view(), name='books-detail'),
    path('<int:pk>/update', views.BooksUpdateView.as_view(), name='book-update'),
    path('<int:pk>/delete', views.BooksDeleteView.as_view(), name='book-delete')
]
