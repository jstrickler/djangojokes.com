from django.db import models

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

    def __str__(self):
        return self.question

class Riddle(models.Model):
    question = models.TextField(max_length=256)
    answer = models.TextField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        db_table = 'riddles'
