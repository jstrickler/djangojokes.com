from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .models import Joke
from .forms import JokeForm

# Create your views here.

class JokeListView(ListView):
    model = Joke

class JokeDetailView(DetailView):
    model = Joke

class JokeCreateView(CreateView):
    model = Joke
    form_class = JokeForm

class JokeUpdateView(UpdateView):
    model = Joke
    form_class = JokeForm

class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')
