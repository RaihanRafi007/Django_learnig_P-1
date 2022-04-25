from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View, TemplateView
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView , CreateView, UpdateView
from first_app import models
from django.urls import reverse_lazy
# Create your views here.


class IndexView(ListView):
    context_object_name = 'musician_list'
    model = models.Musician
    template_name = 'first_app/index.html'
    
class MusicianDetail(DetailView):
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'first_app/musician_details.html'

class AddMusician(CreateView):
    fields = ('first_name', 'last_name', 'instruments')
    model = models.Musician
    template_name = 'first_app/musician_form.html'

class UpdateMusician(UpdateView):
    fields = ('first_name', 'last_name', 'instruments')
    model = models.Musician
    template_name = 'first_app/musician_form.html'

class DeleteMusician(DeleteView):
    context_object_name = 'musician'
    model = models.Musician
    
    template_name = 'first_app/delete_musician.html'

    