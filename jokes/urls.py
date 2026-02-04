from django.urls import path
from .views import (
    JokeListView, 
    JokeDetailView,
    JokeCreateView,
    JokeUpdateView,
    JokeDeleteView,
)

app_name = 'jokes'

urlpatterns = [
    # jokes/joke/1
    path('joke/update/<int:pk>/', JokeUpdateView.as_view(), name="update_by_pk"),
    path('joke/update/<slug>/', JokeUpdateView.as_view(), name="update_by_slug"),
    path('joke/<slug>/delete/', JokeDeleteView.as_view(), name="delete"),
    path('joke/create/', JokeCreateView.as_view(), name="create"),
    path('joke/<slug>', JokeDetailView.as_view(), name='detail'),
    path('', JokeListView.as_view(), name='list'),
]