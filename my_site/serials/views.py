from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Serials, Comment_serial
from .forms import SerialsFrom, CommentSerialForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.views.generic.detail import BaseDetailView


def serials_home(request):
    ser = Serials.objects.order_by('title')
    return render(request, 'serials/serials_home2.html', {'ser': ser})


class SerialsDetailView(DetailView):
    # model = Serials
    # template_name = 'serials/details_view_serial2.html'
    # context_object_name = 'serial'


    def get(self, request, slug, *args, **kwargs):
        serial = get_object_or_404(Serials, url=slug)
        comment_form = CommentSerialForm()
        return render(request, 'serials/details_view_serial2.html', context={
            'serial': serial,
            'comment_form': comment_form
        })

    def post(self, request, slug, *args, **kwargs):
        comment_form = CommentSerialForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['text']
            username = self.request.user
            serial = get_object_or_404(Serials, url=slug)
            comment = Comment_serial.objects.create(serial=serial, username=username, text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/serials'))
        return render(request, 'serials/details_view_serial2.html', context={
            'comment_form': comment_form
        })


class SerialsUpdateView(UpdateView):
    model = Serials
    template_name = 'serials/create.html'

    form_class = SerialsFrom


class SerialsDeleteView(DeleteView):
    model = Serials
    success_url = '/serials'
    template_name = 'serials/serial-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = SerialsFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверно заполнено'

    form = SerialsFrom()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'serials/create.html', data)
