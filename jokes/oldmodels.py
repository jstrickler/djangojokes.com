from django.db import models
from django.urls import reverse

# Create your models here.
class Joke(models.Model):
    question = models.TextField(max_length=256)
    answer = models.TextField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # riddles = models.ForeignKey('Riddle')

    class Meta:
        db_table = 'jokes'
        ordering = ['question', 'answer']
        # ordering = ['-updated', 'question', 'answer']

    def get_absolute_url(self):
        return reverse('jokes:detail', args=[str(self.pk)])

    def __str__(self):
        return self.question
