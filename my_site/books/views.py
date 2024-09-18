from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Books, Comment_books
from .forms import BooksFrom, CommentBookForm
from django.views.generic import DetailView, UpdateView, DeleteView


def books_home(request):
    boo = Books.objects.order_by('title')
    return render(request, 'books/books_home2.html', {'boo': boo})


class BooksDetailView(DetailView):
    # model = Books
    # template_name = 'books/details_view_book2.html'
    # context_object_name = 'book'

    def get(self, request, slug, *args, **kwargs):
        book = get_object_or_404(Books, url=slug)
        comment_form = CommentBookForm()
        return render(request, 'books/details_view_book2.html', context={
            'book': book,
            'comment_form': comment_form
        })

    def post(self, request, slug, *args, **kwargs):
        comment_form = CommentBookForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['text']
            username = self.request.user
            book = get_object_or_404(Books, url=slug)
            comment = Comment_books.objects.create(book=book, username=username, text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/serials'))
        return render(request, 'serials/details_view_serial2.html', context={
            'comment_form': comment_form
        })


class BooksUpdateView(UpdateView):
    model = Books
    template_name = 'books/create.html'

    form_class = BooksFrom


class BooksDeleteView(DeleteView):
    model = Books
    success_url = '/books/'
    template_name = 'books/book-delete.html'


# def create(request):
#     error = ''
#     if request.method == 'POST':
#         form = BooksFrom(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             error = 'Неверно заполнено'
#
#     form = BooksFrom()
#
#     data = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'books/create.html', data)
