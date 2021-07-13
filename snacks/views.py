from django.db.models.base import Model
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy
# Create your views here.

class SnackListView(ListView):
    template_name = "home.html"
    model = Snack
class SnackDetailView(DetailView):
    template_name = "details.html"
    model = Snack
class SnackCreateView(CreateView):
    template_name = 'create.html'
    model = Snack
    fields = ['name', 'purchaser', 'description']
class SnackUpdateView(UpdateView):
    template_name = 'update.html'
    model = Snack
    fields = ['name', 'purchaser', 'description']
class SnackDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Snack
    success_url = reverse_lazy('home')