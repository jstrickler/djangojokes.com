from jokes.models import Joke, Category, Tag
from .serializers import JokeSerializer

from rest_framework.generics import ListAPIView

class JokeListView(ListAPIView):
    queryset = Joke.objects.all()[:10]
    serializer_class = JokeSerializer

