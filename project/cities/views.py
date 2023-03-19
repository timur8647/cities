from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *

from .forms import CityForm
from .models import City

class CitiesListView(ListView):
    paginate_by = 5
    model = City
    template_name = 'Cities/home.html'





class CitiesCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'


class CitisDetailView(DetailView):
    model = City
    template_name = 'cities/detail.html'

class CitiesUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')

class CitiesDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')
# Create your views here.
