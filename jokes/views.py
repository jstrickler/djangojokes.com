import json
from django.http import JsonResponse


from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.messages.views import SuccessMessageMixin

from .models import Joke, JokeVote
from .forms import JokeForm

# Create your views here.

class JokeListView(ListView):
    model = Joke
    paginate_by = 15

class JokeDetailView(DetailView):
    model = Joke

class JokeCreateView(SuccessMessageMixin, CreateView):
    model = Joke
    form_class = JokeForm
    success_message = "Joke added"

class JokeUpdateView(UpdateView):
    model = Joke
    form_class = JokeForm

class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')

# API view
def vote(request, slug):
    user = request.user # The logged-in user (or AnonymousUser).
    joke = Joke.objects.get(slug=slug) # The joke instance.
    data = json.loads(request.body) # Data from the JavaScript.

    # Set simple variables.
    vote = data['vote'] # The user's new vote.
    likes = data['likes'] # The number of likes currently displayed on page.
    dislikes = data['dislikes'] # The number of dislikes currently displayed.

    if user.is_anonymous: # User not logged in. Can't vote.
        msg = 'Sorry, you have to be logged in to vote.'
    else: # User is logged in.
        if JokeVote.objects.filter(user=user, joke=joke).exists():
            # User already voted. Get user's past vote:
            joke_vote = JokeVote.objects.get(user=user, joke=joke)

            if joke_vote.vote == vote: # User's new vote is the same as old vote.
                msg = 'Right. You told us already. Geez.'
            else: # User changed vote.
                joke_vote.vote = vote # Update JokeVote instance.
                joke_vote.save() # Save.

                # Set data to return to the browser.
                if vote == -1:
                    likes -= 1
                    dislikes += 1
                    msg = "Don't like it after all, huh? OK. Noted."
                else:
                    likes += 1
                    dislikes -= 1
                    msg = 'Grown on you, has it? OK. Noted.'
        else: # First time user is voting on this joke.
            # Create and save new vote.
            joke_vote = JokeVote(user=user, joke=joke, vote=vote)
            joke_vote.save()

            # Set data to return to the browser.
            if vote == -1:
                dislikes += 1
                msg = "Sorry you didn't like the joke."
            else:
                likes += 1
                msg = "Yeah, good one, right?"

    # Create object to return to browser.
    response = {
        'msg': msg,
        'likes': likes,
        'dislikes': dislikes
    }
    return JsonResponse(response) # Return object as JSON.