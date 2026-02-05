from django.db import models
from django.urls import reverse
from common.utils.text import unique_slug

# Create your models here.
class Joke(models.Model):
    """
    Joke: A single joke

    A hilarious joke, stored as a question and an answer. Be prepared for
    belly laughts and guffaws. 
    """
    question = models.TextField(max_length=256, help_text="The first part of the joke")
    answer = models.TextField(max_length=100, blank=True, help_text="The second part of the joke")
    rating = models.IntegerField(help_text="Joke rating, from 1 to 10", default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # riddles = models.ForeignKey('Riddle')

    slug = models.SlugField(
        max_length=50, unique=True, editable=False,
        null=False
    )

    # def to_speech(self):
    #     """
    #     Let the user listen to the joke. 
    #     """
    #     pass  # say joke out loud

    def save(self, *args, **kwargs):
        """
        Save record to database. Extends builtin .save() and creates
        the slug field for a joke. 
        """
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))  # Joke??
        super().save(*args, **kwargs) # 


    class Meta:
        db_table = 'jokes'
#        ordering = ['question', 'answer']
        ordering = ['-updated']

    def get_absolute_url(self):
        """
        Create a URL using the joke's slug field. 

        :return _type: A string representing the URL for one joke. 
        """
        return reverse('jokes:detail', args=[str(self.slug)])

    def __str__(self):
        return self.question
